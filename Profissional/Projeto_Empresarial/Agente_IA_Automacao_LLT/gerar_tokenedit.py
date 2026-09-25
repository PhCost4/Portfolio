from google_auth_oauthlib.flow import InstalledAppFlow
import json

# Scope de ESCRITA no Drive (diferente do token de leitura)
SCOPES = [
    'https://www.googleapis.com/auth/drive'
]

# Abre navegador para autorizar — use o credentials do Cliente de computador 2
flow = InstalledAppFlow.from_client_secrets_file(
    'credentialsOutput2.json', SCOPES)
creds = flow.run_local_server(port=0)

# Exibe o token para copiar no GitHub Secrets
print("=== COPIE TUDO ABAIXO PARA O SECRET GOOGLE_TOKEN_2 ===")
print(creds.to_json())