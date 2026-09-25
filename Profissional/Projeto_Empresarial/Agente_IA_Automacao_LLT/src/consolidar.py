# =============================================================
#  CONSOLIDAR.PY — Previsão Passageiros LLT Lounge
#  Versão: 1.3 | Atualizado: 2026
# =============================================================
#
#  MANUTENÇÃO: Todas as configurações estão no bloco abaixo.
#  Nunca altere fora deste bloco a menos que a lógica mude.
#
# =============================================================

import gspread
import pandas as pd
import json
import os
import io
import openpyxl
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from datetime import datetime

# ╔═══════════════════════════════════════════════════════════╗
# ║              BLOCO DE CONFIGURAÇÕES                       ║
# ║  Toda manutenção futura deve ser feita APENAS AQUI        ║
# ╚═══════════════════════════════════════════════════════════╝

# ─────────────────────────────────────────────────────────────
# [CONFIG 1] Nome da aba na planilha da Latam
# Manutenção: atualizar se a Latam renomear a aba
# ─────────────────────────────────────────────────────────────
NOME_ABA = 'PREVISTO X REALIZADO 2026'

# ─────────────────────────────────────────────────────────────
# [CONFIG 2] Blocos de meses da planilha
# Formato: (coluna_inicio, coluna_fim, ano, mes_numero, nome_mes)
# Manutenção: adicionar novos meses ou corrigir posições
#             se a Latam inserir/remover colunas na planilha
# ─────────────────────────────────────────────────────────────
MESES = [
    (0,  4,  2026, 1,  "jan"),   # Colunas A-E   → Janeiro 2026
    (6,  10, 2026, 2,  "fev"),   # Colunas G-K   → Fevereiro 2026
    (12, 16, 2026, 3,  "mar"),   # Colunas M-Q   → Março 2026
    (18, 22, 2026, 4,  "abr"),   # Colunas S-W   → Abril 2026
    (24, 28, 2026, 5,  "mai"),   # Colunas Y-AC  → Maio 2026
    (30, 34, 2026, 6,  "jun"),   # Colunas AE-AI → Junho 2026
    (36, 40, 2026, 7,  "jul"),   # Colunas AK-AO → Julho 2026
    (42, 46, 2026, 8,  "ago"),   # Colunas AQ-AU → Agosto 2026
    (48, 52, 2026, 9,  "set"),   # Colunas AW-BA → Setembro 2026
    (54, 58, 2026, 10, "out"),   # Colunas BC-BG → Outubro 2026
    (60, 64, 2026, 11, "nov"),   # Colunas BI-BM → Novembro 2026
    (66, 70, 2026, 12, "dez"),   # Colunas BO-BS → Dezembro 2026
    # ── 2027: descomentar e adicionar nova aba quando necessário ──
    # (0, 4, 2027, 1, "jan"),
    # (6, 10, 2027, 2, "fev"),
]

# ─────────────────────────────────────────────────────────────
# [CONFIG 3] Formato da data nas células da planilha
# Manutenção: atualizar se a Latam mudar o formato das datas
# Exemplos: "%d/%m" | "%d-%m" | "%Y-%m-%d"
# ─────────────────────────────────────────────────────────────
FORMATO_DATA_ENTRADA = "%d/%m/%Y"   # ex: "01/01/2026" (após concatenar ano)
FORMATO_DATA_SAIDA   = "%Y-%m-%d"   # ex: "2026-01-01" (padrão final)

# ─────────────────────────────────────────────────────────────
# [CONFIG 4] Valores que devem ser ignorados na coluna Data
# Manutenção: adicionar novos valores se a planilha ganhar
#             cabeçalhos intermediários ou textos extras
# ─────────────────────────────────────────────────────────────
VALORES_IGNORAR = {'', 'DIAS', 'None', 'none', 'DATA', 'Data', '-'}

# ─────────────────────────────────────────────────────────────
# [CONFIG 5] Faixas de preço (Column Expressions do KNIME)
# Manutenção: atualizar faixas e valores se a tabela de
#             preços mudar — formato: (limite, preco)
#             O último item é o valor padrão (sem limite)
# ─────────────────────────────────────────────────────────────
FAIXAS_PRECO = [
    (37500, 65.35),   # Realizado < 37500  → R$ 65,35
    (40000, 64.24),   # Realizado < 40000  → R$ 64,24
    (42500, 63.37),   # Realizado < 42500  → R$ 63,37
    (None,  69.40),   # Realizado >= 42500 → R$ 69,40
]

# ─────────────────────────────────────────────────────────────
# [CONFIG 6] Nome do arquivo de saída
# Manutenção: atualizar se quiser mudar o nome do arquivo
#             gerado e enviado ao Google Drive
# ─────────────────────────────────────────────────────────────
NOME_ARQUIVO_SAIDA = 'Previsao_Passageiros_LLT_GitHub.xlsx'

# ─────────────────────────────────────────────────────────────
# [CONFIG 7] Colunas finais e ordem de exibição
# Manutenção: adicionar/remover/reordenar colunas no output
# ─────────────────────────────────────────────────────────────
COLUNAS_FINAIS = ['Data', 'Previsão', 'Realizado', 'Variação', 'DataMes', 'Preço']

# ╔═══════════════════════════════════════════════════════════╗
# ║              FIM DO BLOCO DE CONFIGURAÇÕES                ║
# ║  Não altere o código abaixo sem necessidade               ║
# ╚═══════════════════════════════════════════════════════════╝

# ─────────────────────────────────────────────────────────────
# IDs das planilhas (lidos dos secrets do GitHub Actions)
# ─────────────────────────────────────────────────────────────
SHEET_ID   = os.environ.get('SHEET_ID', '')    # Planilha de leitura (Latam) — agora .xlsx
SHEET_ID_2 = os.environ.get('SHEET_ID_2', '')  # Pasta/destino no Google Drive


# ─────────────────────────────────────────────────────────────
# AUTENTICAÇÃO GOOGLE — Leitura (GOOGLE_TOKEN)
# ─────────────────────────────────────────────────────────────
SCOPES_LEITURA = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]

def autenticar_creds():
    """Retorna credentials puras (usadas para Drive API)."""
    token_info = json.loads(os.environ['GOOGLE_TOKEN'])
    creds = Credentials.from_authorized_user_info(token_info, SCOPES_LEITURA)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        print("Token renovado automaticamente.")
    return creds


# ─────────────────────────────────────────────────────────────
# LEITURA DO .XLSX VIA GOOGLE DRIVE API
# ─────────────────────────────────────────────────────────────
def ler_xlsx_do_drive(file_id, nome_aba):
    """Baixa o .xlsx do Drive pelo ID e retorna todas as linhas da aba especificada."""
    creds   = autenticar_creds()
    service = build('drive', 'v3', credentials=creds)

    request    = service.files().get_media(fileId=file_id)
    buffer     = io.BytesIO()
    downloader = MediaIoBaseDownload(buffer, request)

    done = False
    while not done:
        _, done = downloader.next_chunk()

    buffer.seek(0)
    wb = openpyxl.load_workbook(buffer, data_only=True)
    ws = wb[nome_aba]

    todas_linhas = []
    for row in ws.iter_rows(values_only=True):
        linha_tratada = []
        for c in row:
            if c is None:
                linha_tratada.append('')
            elif isinstance(c, datetime):
                # ✅ Converte datetime para "dd/mm" (formato esperado pelo processar_mes)
                linha_tratada.append(c.strftime("%d/%m"))
            else:
                linha_tratada.append(str(c))
        todas_linhas.append(linha_tratada)

    print(f"Arquivo .xlsx lido com sucesso via Drive API: {len(todas_linhas)} linhas")
    return todas_linhas


# ─────────────────────────────────────────────────────────────
# CÁLCULO DE PREÇO
# ─────────────────────────────────────────────────────────────
def calcular_preco(soma_mes):
    """Aplica as faixas de preço com base na SOMA do Realizado do mês (CONFIG 5)."""
    try:
        valor = float(soma_mes)
        for limite, preco in FAIXAS_PRECO:
            if limite is None or valor < limite:
                return preco
    except:
        return None


# ─────────────────────────────────────────────────────────────
# PROCESSAMENTO DE CADA MÊS
# ─────────────────────────────────────────────────────────────
def processar_mes(todas_linhas, col_inicio, col_fim, ano, mes_num, nome_mes):
    """Extrai e trata os dados de um bloco de mês da planilha."""
    registros    = []
    data_mes_str = f"{nome_mes}/{str(ano)[2:]}"  # ex: jan/26

    for linha in todas_linhas[2:]:  # Pula linha 1 (mês) e linha 2 (cabeçalho)
        if len(linha) <= col_fim:
            continue

        bloco = linha[col_inicio:col_fim + 1]
        if len(bloco) < 5:
            continue

        # Posições relativas dentro do bloco de cada mês
        data_raw  = str(bloco[1]).strip()   # coluna DIAS
        previsto  = str(bloco[2]).strip()   # coluna PREVISTO
        realizado = str(bloco[3]).strip()   # coluna REALIZADO
        variacao  = str(bloco[4]).strip()   # coluna VARIAÇÃO

        # Row Filter — ignora linhas inválidas (CONFIG 4)
        if data_raw in VALORES_IGNORAR:
            continue

        # Monta e converte a data completa (CONFIG 3)
        try:
            data_completa  = f"{data_raw}/{ano}"
            data_dt        = datetime.strptime(data_completa, FORMATO_DATA_ENTRADA)
            data_formatada = data_dt.strftime(FORMATO_DATA_SAIDA)
        except:
            continue

        # ✅ CORREÇÃO 1: Converte para número usando float() antes do int()
        # Evita problema com "2000.0" virando "20000" após replace de ponto
        try:
            previsto_num = int(float(str(previsto).replace(',', '.')))
        except:
            previsto_num = None

        try:
            realizado_num = int(float(str(realizado).replace(',', '.')))
        except:
            realizado_num = None

        # Filtro — só inclui linha se Previsão E Realizado estiverem preenchidos
        if previsto_num is None and realizado_num is None:
            continue

        # ✅ CORREÇÃO 2: Converte variação de decimal para percentual
        # O openpyxl lê células de % como decimal (ex: 0.0162 → 1.62%)
        # Também trata erros #DIV/0!
        if '#DIV' in variacao or variacao in {'#DIV/0!', '#DIV/0'}:
            variacao_final = None
        else:
            try:
                variacao_final = round(float(variacao) * 100, 2)  # ex: 0.0162 → 1.62
            except:
                variacao_final = None

        registros.append({
            'Data':      data_formatada,
            'Previsão':  previsto_num,
            'Realizado': realizado_num,
            'Variação':  variacao_final,
            'DataMes':   data_mes_str,
            'Preço':     None  # será preenchido após somar o mês
        })

    # Calcula preço com base na SOMA do Realizado do mês (CONFIG 5)
    soma_realizado_mes = sum(
        r['Realizado'] for r in registros if r['Realizado'] is not None
    )
    preco_mes = calcular_preco(soma_realizado_mes) if soma_realizado_mes > 0 else None

    for r in registros:
        r['Preço'] = preco_mes

    return registros


# ─────────────────────────────────────────────────────────────
# CONSOLIDAÇÃO PRINCIPAL
# ─────────────────────────────────────────────────────────────
def consolidar():
    print("=" * 55)
    print("  Consolidação — Previsão Passageiros LLT Lounge")
    print("=" * 55)

    # Lê o .xlsx diretamente do Drive via API (substituiu gspread)
    todas_linhas = ler_xlsx_do_drive(SHEET_ID, NOME_ABA)
    print(f"Linhas lidas da planilha: {len(todas_linhas)}")

    # Processa cada mês (CONFIG 2)
    todos_registros = []
    for col_ini, col_fim, ano, mes_num, nome_mes in MESES:
        registros = processar_mes(todas_linhas, col_ini, col_fim, ano, mes_num, nome_mes)
        if registros:
            print(f"  {nome_mes}/{str(ano)[2:]}: {len(registros)} registros")
            todos_registros.extend(registros)

    if not todos_registros:
        print("Nenhum registro encontrado. Verifique a planilha.")
        return None

    df_novo = pd.DataFrame(todos_registros)[COLUNAS_FINAIS]  # CONFIG 7
    print(f"\nTotal consolidado: {len(df_novo)} registros")

    # ── Lógica de acumulação ──────────────────────────────────
    # Primeira execução: cria arquivo novo
    # Execuções seguintes: atualiza mantendo histórico anterior
    # ─────────────────────────────────────────────────────────
    if os.path.exists(NOME_ARQUIVO_SAIDA):
        print("Arquivo existente encontrado — atualizando...")
        df_existente = pd.read_excel(NOME_ARQUIVO_SAIDA)
        meses_novos  = df_novo['DataMes'].unique()

        # Remove meses que serão substituídos para evitar duplicatas
        df_existente = df_existente[~df_existente['DataMes'].isin(meses_novos)]
        df_final     = pd.concat([df_existente, df_novo], ignore_index=True)
        df_final     = df_final.sort_values('Data').reset_index(drop=True)
    else:
        print("Primeira execução — criando arquivo novo...")
        df_final = df_novo

    df_final.to_excel(NOME_ARQUIVO_SAIDA, index=False)
    print(f"Arquivo salvo: {NOME_ARQUIVO_SAIDA} ({len(df_final)} registros totais)")
    return NOME_ARQUIVO_SAIDA


# ─────────────────────────────────────────────────────────────
# ENVIO PARA O GOOGLE DRIVE
# ─────────────────────────────────────────────────────────────
def enviar_google_drive(arquivo_local):
    from googleapiclient.http import MediaFileUpload

    token_info = json.loads(os.environ['GOOGLE_TOKEN_2'])
    creds = Credentials.from_authorized_user_info(token_info, [
        'https://www.googleapis.com/auth/drive'
    ])
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        print("Token_2 renovado automaticamente.")

    service = build('drive', 'v3', credentials=creds)

    media = MediaFileUpload(
        arquivo_local,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    # Se o secret DRIVE_FILE_ID estiver definido, atualiza direto pelo ID fixo
    drive_file_id = os.environ.get('DRIVE_FILE_ID', '').strip()

    if drive_file_id:
        service.files().update(fileId=drive_file_id, media_body=media).execute()
        print(f"Arquivo atualizado no Google Drive (ID fixo: {drive_file_id})")
    else:
        query = (f"name='{os.path.basename(arquivo_local)}' "
                 f"and '{SHEET_ID_2}' in parents "
                 f"and trashed=false")
        resultados = service.files().list(q=query, fields="files(id, name)").execute()
        arquivos   = resultados.get('files', [])

        if arquivos:
            file_id = arquivos[0]['id']
            service.files().update(fileId=file_id, media_body=media).execute()
            print(f"Arquivo atualizado no Google Drive: {arquivos[0]['name']}")
            print(f">>> DRIVE_FILE_ID={file_id} <<< salve este ID no secret DRIVE_FILE_ID")
        else:
            metadata = {
                'name': os.path.basename(arquivo_local),
                'parents': [SHEET_ID_2]
            }
            resultado = service.files().create(body=metadata, media_body=media, fields='id,name').execute()
            file_id   = resultado.get('id')
            print(f"Arquivo criado no Google Drive!")
            print(f">>> DRIVE_FILE_ID={file_id} <<< salve este ID no secret DRIVE_FILE_ID")


# ─────────────────────────────────────────────────────────────
# EXECUÇÃO
# ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    arquivo = consolidar()
    if arquivo:
        enviar_google_drive(arquivo)