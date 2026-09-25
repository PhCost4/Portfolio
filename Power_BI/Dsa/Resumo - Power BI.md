# Power BI — Resumo do Curso

*Conceitos, boas práticas e anotações de estudo*

Curso: Formação Power BI — Data Science Academy (DSA)

Autor das anotações: Pedro

***OBS: em qualquer projeto ou situação-problema, o primeiro passo é sempre entender o problema proposto — só depois identificar quais informações usar e quais perguntas fazer.***

## Sumário

- [Capítulos 1 e 2 — Introdução ao Power BI](#capítulos-1-e-2--introdução-ao-power-bi)

- [Capítulo 3 — Modelagem de Dados, Relações e DAX](#capítulo-3--modelagem-de-dados-relações-e-expressões-dax)

- [Capítulo 4 — Power BI para Análise de Marketing](#capítulo-4--power-bi-para-análise-de-marketing)

- [Capítulo 5 — Análise de Dados Comerciais](#capítulo-5--análise-de-dados-comerciais)

- [Capítulo 6 — Análise de RH](#capítulo-6--análise-de-rh)

- [Capítulo 7 — Logística](#capítulo-7--logística)

- [Capítulo 8 — Análise de Dados Financeiros](#capítulo-8--análise-de-dados-financeiros)

- [Capítulo 9 — Relatórios de Contabilidade](#capítulo-9--relatórios-de-contabilidade)

- [Capítulo 10 — Mercado de Ações (Time Intelligence)](#capítulo-10--mercado-de-ações-time-intelligence)

- [Capítulo 11 — Conceitos de Estatística](#capítulo-11--conceitos-de-estatística)

- [Capítulo 12 — Limpeza e Manutenção de Dados](#capítulo-12--limpeza-e-manutenção-de-dados)

- [Capítulo 13 — Manipulação de Dados com Power Query e Linguagem M](#capítulo-13--manipulação-de-dados-com-power-query-e-linguagem-m)

- [Capítulo 14 — Power BI e Banco de Dados](#capítulo-14--power-bi-e-banco-de-dados)

- [Capítulo 15 — SQL Analytics](#capítulo-15--sql-analytics)

- [Capítulo 16 — Machine Learning para Segmentação de Clientes (Python)](#capítulo-16--machine-learning-para-segmentação-de-clientes-python)

- [Capítulo 17 — Machine Learning para Detecção de Anomalias (R)](#capítulo-17--machine-learning-para-detecção-de-anomalias-r)

- [Capítulo 18 — Inteligência Artificial e Análise de Séries Temporais](#capítulo-18--inteligência-artificial-e-análise-de-séries-temporais)

## Capítulos 1 e 2 — Introdução ao Power BI

O início do aprendizado em Power BI envolve compreender os principais tipos de visualizações e como aplicá-las de forma eficiente.

Tipos de gráficos e quando usar

-   **Gráfico Cartão:** ideal utilizar apenas 1 métrica; destaca uma informação principal de forma clara.

-   **Gráfico Pizza:** recomendado para até 2 métricas, com poucas categorias; útil para mostrar proporções.

-   **Gráfico de Barra Empilhada:** ideal para até 3 métricas; permite comparar partes dentro de um todo.

-   **Gráfico de Barra:** indicado para grandes volumes de dados; facilita a comparação entre categorias.

-   **Gráfico de Mapa:** demonstra informações geograficamente, ideal para análises regionais.

> **📌 Complemento:** *Como regra geral, quanto menos categorias e métricas em um gráfico, mais fácil a leitura — cartões e pizzas pedem poucas variáveis; barras e mapas suportam volumes maiores.*

Dicas importantes ao criar dashboards

-   Extrair o máximo de informações do gestor ou cliente, garantindo que o dashboard responda a necessidades reais.

-   Sempre partir de perguntas ou situações-problema para definir quais dados e gráficos serão necessários.

-   Antes de inserir dados no Power BI, realizar tratamento prévio com Power Query: formatar, segmentar e analisar.

-   Ao finalizar o dashboard, conferir se as informações estão claras, objetivas e correspondem às situações-problema levantadas.

## Capítulo 3 — Modelagem de Dados, Relações e Expressões DAX

A modelagem de dados é essencial para uma análise eficiente no Power BI.

Conceitos fundamentais

-   **Modelagem de dados:** definição de tabelas, colunas e relações entre elas.

-   **Aplicações do BI:** analisar dados passados para apoiar a tomada de decisão.

-   **Data Science:** prever cenários futuros com base em dados históricos.

-   **Cardinalidade:** usar sempre "1 para 1" para evitar inconsistências; quando houver "muitos para muitos", criar tabelas intermediárias (ponte).

-   **Limpeza e transformação:** remover duplicatas, cortar espaços e caracteres desnecessários.

Gráficos específicos

-   **Cascata (Waterfall):** bom para poucas categorias (5 a 7); mostra a variação acumulada entre valores.

-   **Treemap:** similar ao gráfico de pizza, mas suporta mais categorias, organizadas em blocos proporcionais.

-   **KPI:** indica o desempenho em relação a uma meta.

-   **Segmentação de dados (slicers):** filtros visuais para análises rápidas.

-   **Gráfico de dispersão:** útil para analisar a relação entre duas variáveis.

-   **Gráfico de árvore hierárquica:** ideal para mostrar métricas em níveis diferentes (drill down).

DAX e boas práticas

-   Funções DAX permitem criar filtros, agrupamentos e cálculos complexos — por exemplo, médias ponderadas com SUMX.

-   Boas práticas de dashboard: usar poucos gráficos (no máximo 5 a 6) e sempre verificar a clareza da leitura.

> **📌 Complemento:** *DAX (Data Analysis Expressions) é a linguagem de fórmulas do Power BI usada para criar colunas calculadas, medidas e tabelas — diferente da linguagem M, que atua na etapa de transformação dos dados (Power Query).*

O que é modelagem de dados, afinal?

Modelagem de dados é o processo de criar uma representação visual, ou esquema, que define os sistemas de coleta e gerenciamento de informações de uma organização. Esse "blueprint" ajuda diferentes perfis — Analistas de Dados, Cientistas de Dados, Arquitetos de Dados e Engenheiros de Dados — a construir uma visão unificada dos dados, descrevendo quais dados a empresa coleta, como os diferentes conjuntos de dados se relacionam entre si e quais métodos serão usados para armazenar e analisar essas informações.

Esse processo costuma ser dividido em três níveis:

-   **Modelo conceitual:** define os conceitos do negócio e as relações entre eles, sem se preocupar ainda com a implementação técnica.

-   **Modelo lógico:** especifica como os dados serão armazenados e como as relações serão representadas dentro de um banco de dados.

-   **Modelo físico:** descreve como os dados serão efetivamente armazenados em um sistema de armazenamento específico.

Modelagem de dados dentro do Business Intelligence

Business Intelligence (BI) combina análise de negócios, mineração de dados, visualização de dados e infraestrutura de dados para ajudar as organizações a tomar decisões orientadas por dados, com foco em analisar o passado — métricas, indicadores, padrões e relacionamentos. Data Science, por sua vez, tem foco maior na análise preditiva, buscando compreender o que pode acontecer no futuro.

A modelagem de dados é peça central do BI porque garante que os dados fiquem armazenados de forma organizada e consistente, facilitando a recuperação e a análise. Entre as formas mais comuns de aplicá-la estão:

-   **Data Warehouse (DW):** repositório centralizado de dados de negócio usado para suportar análise e tomada de decisão.

-   **Modelo Estrela (Star Schema):** técnica de modelagem comumente usada para projetar um DW, garantindo consistência e facilidade de acesso aos dados.

-   **Cubos multidimensionais:** estruturas que ajudam a agregar e analisar dados vindos de várias fontes.

-   **Otimização de consultas:** a modelagem também garante que as consultas ao Data Warehouse sejam executadas de forma eficiente.

-   **Integração e governança de dados:** unificação de dados de fontes diferentes com consistência e qualidade, incluindo rastreamento de alterações e auditoria.

Modelagem de dados no Power BI, na prática

O Power BI simplifica bastante esse processo, criando um modelo de dados básico — porém eficiente — que já pode ser usado para analisar as informações corretamente, e evita erros de relacionamento quando os dados estão bem organizados. Importante: o Power BI não cria os relacionamentos entre os dados automaticamente se eles não estiverem corretamente conectados (embora ainda seja possível montar gráficos e dashboards mesmo sem esse relacionamento ideal).

Na prática, a modelagem de dados dentro do Power BI aparece em pontos como:

-   **Importação de dados:** o Power BI permite importar dados de fontes variadas (bancos de dados, arquivos, serviços na nuvem); a modelagem prepara esses dados para que fiquem em um formato consistente e estruturado.

-   **Criação de tabelas e relações:** garante que os dados fiquem organizados de forma lógica e coerente entre si.

-   **Medidas e cálculos:** a modelagem garante que somas, médias, percentuais e outros cálculos personalizados sejam aplicados de forma consistente.

-   **Filtros e segmentação:** permitem que os usuários explorem os dados de forma mais precisa e detalhada.

-   **Publicação de relatórios e dashboards:** tudo isso baseado no modelo de dados construído, para que outros usuários possam acessar e explorar com facilidade.

> **💡 Dica:** *Sempre verifique o modelo de dados no Power BI quando estiver usando mais de uma fonte de dados. Compreenda os relacionamentos de negócio (por exemplo: um produto pode estar associado a mais de uma venda) e, se necessário, desmembre uma única planilha ou tabela em partes diferentes para construir o relacionamento adequado antes de seguir com a análise.*
>
> **🛠️ Prática aplicada no curso:** *Lab 1 — Dashboard Analítico de Vendas Globais, aplicando na prática os conceitos de modelagem de dados vistos neste capítulo.*

## Capítulo 4 — Power BI para Análise de Marketing

Existem diversos indicadores de marketing que as empresas usam para medir o sucesso de suas estratégias e campanhas.

Principais KPIs de Marketing

-   **Taxa de conversão:** proporção de visitantes do site que realizam uma ação desejada, como comprar um produto ou preencher um formulário de contato.

-   **Taxa de retenção do cliente:** proporção de clientes que compram novamente.

-   **Custo por Aquisição de Cliente (CAC):** custo total de adquirir um novo cliente, incluindo despesas com publicidade e marketing.

-   **Retorno sobre Investimento (ROI):** lucro ou prejuízo obtido em relação ao investimento feito em uma campanha.

-   **Conscientização da marca:** medida da familiaridade e do reconhecimento da marca entre o público-alvo.

-   **Engajamento:** medida da interação dos usuários com conteúdo, campanhas e canais de marketing.

-   **Net Promoter Score (NPS):** medida da lealdade dos clientes, baseada na disposição de recomendar a empresa ou produto.

-   **Tráfego do website:** número de visitas ao site.

Esses indicadores devem ser monitorados regularmente para ajudar as empresas a entender o sucesso de suas estratégias e fazer ajustes onde for necessário. Também é importante compreender o perfil dos clientes, o comportamento de gastos e os padrões de compra de acordo com diferentes métricas.

Tratamento de variáveis

-   Variáveis binárias: "Sim" = 1, "Não" = 0; podem ser usadas em funções IF.

-   Ajustar os tipos de variáveis (numérico, texto, etc.) para garantir consistência nos cálculos.

-   **Gráfico Matrix:** mostra colunas com diferentes valores, útil para comparações cruzadas.

-   Remoção de outliers: essencial para garantir análises precisas.

> **🛠️ Prática aplicada no curso:** *Mini-Projeto 1 — Análise de Campanhas de Marketing com Power BI, cobrindo visão do cliente, comportamento de compra, performance das campanhas e padrões de compra por país.*

## Capítulo 5 — Análise de Dados Comerciais

Os principais KPIs da área comercial medem o desempenho e a eficiência das atividades de vendas.

Principais KPIs comerciais

-   **Volume de vendas:** quantidade de produtos ou serviços vendidos.

-   **Ticket médio:** valor médio das vendas por transação.

-   **Taxa de conversão:** proporção de visitantes ou contatos que se tornam clientes.

-   **Ciclo de vendas:** tempo médio para fechar uma venda, do primeiro contato até o fechamento.

-   **Retenção de clientes:** taxa de clientes que compram novamente após a primeira compra.

-   **Lucratividade:** receita líquida obtida pela venda de produtos ou serviços, descontados os custos.

-   **Produtividade da equipe de vendas:** quantidade de vendas realizadas por vendedor, por período.

-   **Satisfação do cliente:** medida da satisfação com a empresa, os produtos e os serviços oferecidos.

Esses KPIs ajudam a identificar pontos fortes e fracos na estratégia de vendas e permitem tomar decisões mais informadas para melhorar o desempenho da área comercial.

Recursos e boas práticas

-   **Narrativa Inteligente:** resume os relatórios em uma única visualização, facilitando a interpretação.

-   Identificação dos principais influenciadores de vendas: fatores que impactam os resultados.

-   Faixas de vendas: segmentação por categoria ou produto.

-   Performance por região: avaliação do desempenho de vendedores por área geográfica.

-   **Gráficos:** funil para poucas categorias; faixa/range para a área comercial; algumas visualizações podem precisar de escala maior.

-   **Índice e navegação:** botões que facilitam a movimentação entre páginas do relatório.

-   **Engenharia de atributos:** criação de novas colunas ou medidas para análises mais detalhadas.

-   Classificação de variáveis: quantitativa ou qualitativa.

> **🛠️ Prática aplicada no curso:** *Mini-Projeto 2 — Dashboard Comercial de Performance de Vendas, incluindo narrativa inteligente, principais influenciadores de vendas, faixas de vendas por categoria e performance dos vendedores por região.*

## Capítulo 6 — Análise de RH

Na área de Recursos Humanos, os KPIs ajudam a avaliar o sucesso de processos ligados a pessoas e à gestão de equipes.

Principais KPIs de RH

-   **Taxa de rotatividade (turnover):** mede a frequência com que os funcionários deixam a empresa; pode indicar problemas de ambiente de trabalho, remuneração ou oportunidades de desenvolvimento.

-   **Satisfação do funcionário:** mede o grau de satisfação em relação ao trabalho, remuneração, ambiente e oportunidades de desenvolvimento.

-   **Tempo médio para preenchimento de vagas:** mede o tempo necessário para preencher uma vaga aberta, indicando a eficiência do recrutamento e seleção.

-   **Custo de contratação por funcionário:** custo total de contratar um novo funcionário, incluindo anúncios, entrevistas, testes e treinamento.

-   **Participação em treinamentos:** mede o número de funcionários que participam de programas de desenvolvimento.

-   **Avaliação de desempenho:** avalia o funcionário em um ciclo de trabalho, normalmente de 6 ou 12 meses.

-   **Nível de absenteísmo:** mede a frequência com que os funcionários faltam ao trabalho; pode indicar problemas de ambiente ou saúde.

-   **Nível de engajamento:** escala que define o quão engajados os funcionários estão, geralmente combinando absenteísmo, pontualidade e avaliação de desempenho.

Cada empresa pode ter necessidades e objetivos diferentes, e os KPIs de RH devem ser ajustados de acordo com o contexto específico da organização.

Métricas no Power BI

-   Desenvolvimento de métricas para análise de pessoas usando as funções COUNTROWS, CALCULATE, DIVIDE e AVERAGE.

-   Essas funções são essenciais para o monitoramento de desempenho, absenteísmo e métricas de produtividade.

> **🛠️ Prática aplicada no curso:** *Mini-Projeto 3 — Análise de Dados de RH com Power BI.*

## Capítulo 7 — Logística

Existem diversos KPIs usados para medir a eficácia e a eficiência da área de logística de uma empresa.

Principais KPIs de Logística

-   **Tempo de ciclo:** tempo necessário para atender um pedido, do momento em que é feito até a entrega ao cliente.

-   **Taxa de entrega no prazo:** porcentagem de pedidos entregues dentro do prazo acordado.

-   **Custo de transporte:** custo médio por unidade ou por pedido para transportar os produtos.

-   **Nível de estoque:** número de dias ou semanas de suprimento de estoque disponível.

-   **Taxa de devolução:** porcentagem de pedidos devolvidos pelos clientes.

-   **Índice de acurácia de estoque:** precisão do estoque registrado em relação ao estoque real.

-   **Taxa de utilização de armazenamento:** porcentagem do espaço de armazenamento disponível que está sendo utilizado.

-   **Nível de serviço ao cliente:** satisfação geral com o serviço de logística, incluindo tempo de entrega e atendimento.

-   **Taxa de ocorrência de avarias:** porcentagem de produtos que sofrem danos durante transporte ou armazenamento.

-   **Índice de ROI em logística:** retorno financeiro gerado pelos investimentos em logística, como sistemas de gestão de armazéns.

Monitorar e medir esses KPIs permite que a área de logística avalie sua eficácia e identifique oportunidades de melhoria.

Boas práticas no Power BI

-   Identificar erros e problemas nos dashboards, anotando e justificando cada ajuste feito.

-   **Fonte de dados:** ajustar os caminhos dos datasets no Power BI para evitar inconsistências.

-   Criação de medidas: reduz erros e facilita a manutenção do modelo.

-   **Funções importantes:** COUNTROWS, CALCULATE e FILTER.

-   Avaliar o uso de tabelas ou matrizes para grandes volumes de dados.

-   **Rating:** visual para medir desempenho ou classificação usando estrelas.

> **🛠️ Prática aplicada no curso:** *Mini-Projeto 4 — Desconstruindo o dashboard e resolvendo problemas de análise na área de Logística.*

## Capítulo 8 — Análise de Dados Financeiros

Os KPIs financeiros são métricas importantes para monitorar a saúde financeira de uma empresa.

Principais KPIs financeiros

-   **Fluxo de caixa:** medida do dinheiro que entra e sai da empresa em um período; um fluxo positivo indica receita suficiente para cobrir as despesas.

-   **Margem de lucro:** porcentagem de lucro obtida em cada venda, calculada dividindo o lucro líquido pela receita total.

-   **Retorno sobre Investimento (ROI):** retorno obtido pela empresa em relação aos investimentos feitos, calculado dividindo o lucro pelo investimento inicial.

-   **Endividamento:** quantidade de dívida em relação ao patrimônio líquido, calculado dividindo a dívida total pelo patrimônio líquido.

-   **Faturamento:** receita total gerada pela empresa em um determinado período.

-   **Custo de Aquisição de Clientes (CAC):** valor gasto para adquirir cada novo cliente, dividindo o custo total de marketing e vendas pelo número de novos clientes.

-   **Prazo Médio de Pagamento (PMP):** tempo médio que a empresa leva para pagar seus fornecedores.

Existem muitos outros KPIs financeiros relevantes, que variam conforme as necessidades e objetivos de cada empresa.

Aplicação no Power BI

-   Organização de dados financeiros usando tabelas dinâmicas (pivot tables).

-   Medidas financeiras: receitas, despesas, lucros e margens.

-   Hierarquia de variáveis categóricas para análises mais detalhadas.

-   Uso de principais influenciadores: segmentação de dados para apoiar decisões estratégicas.

> **🛠️ Prática aplicada no curso:** *Mini-Projeto 5 — Dashboard de Análise Financeira com Power BI.*

## Capítulo 9 — Relatórios de Contabilidade

Existem diversos relatórios contábeis que fornecem informações financeiras vitais para as empresas.

Principais relatórios contábeis

-   **Balanço Patrimonial (BP):** apresenta a posição financeira da empresa em um determinado momento: ativos (bens e direitos), passivos (obrigações) e patrimônio líquido.

-   **Demonstração do Resultado do Exercício (DRE):** apresenta o resultado das operações durante um período: receitas, despesas e lucro líquido (ou prejuízo).

-   **Demonstração do Fluxo de Caixa (DFC):** apresenta as entradas e saídas de caixa da empresa e o saldo final do período.

-   **Demonstrativo de Lucros ou Prejuízos Acumulados (DLPA):** indica as mudanças e aplicações do patrimônio líquido durante o período, derivando do DRE e do balanço patrimonial; é obrigatório para sociedades limitadas.

-   **Relatório de Análise de Desempenho:** análise detalhada dos resultados financeiros, comparando com períodos anteriores e com outras empresas do setor.

-   **Notas Explicativas:** informações adicionais que acompanham os relatórios financeiros, detalhando políticas contábeis e operações.

Recursos no Power BI

-   Elaboração de um Balanço Patrimonial no Power BI.

-   **Hierarquia de dados:** uso de drill down e drill up para navegação detalhada.

-   Habilitar a barra de dados na matriz para reforçar a leitura visual dos valores.

-   Automatização de tabelas dinâmicas para otimizar a análise e a atualização dos dados.

> **🛠️ Prática aplicada no curso:** *Lab 3 — Balanço Patrimonial com visual de Matriz no Power BI, aplicando hierarquia de dados e drill down/drill up.*

## Capítulo 10 — Mercado de Ações (Time Intelligence)

Neste capítulo o foco é a Time Intelligence (Inteligência de Tempo) do Power BI, aplicada à análise de dados do mercado de ações.

-   **Medida rápida (Quick Measure):** recurso do Power BI que gera automaticamente fórmulas DAX prontas para cálculos comuns, como acumulado no ano, comparação com período anterior ou média móvel.

-   **Time Intelligence:** conjunto de funções DAX (como TOTALYTD, SAMEPERIODLASTYEAR, DATEADD) que permite analisar os dados ao longo do tempo — comparando dias, meses, trimestres e anos entre si.

> **📌 Complemento:** *Para o Time Intelligence funcionar corretamente, o modelo precisa de uma tabela calendário (tabela de datas) marcada como tabela de datas no Power BI, com uma coluna contínua de datas sem lacunas.*
>
> **🛠️ Prática aplicada no curso:** *Mini-Projeto 6 — Dashboard Analítico do Mercado de Ações com Narrativa Inteligente.*

## Capítulo 11 — Conceitos de Estatística

Estatística Descritiva x Estatística Inferencial

-   **Estatística Descritiva:** foca na organização, resumo e apresentação dos dados de maneira eficiente, utilizando gráficos, tabelas e medidas numéricas como média, mediana, moda, variância e desvio padrão. É o tipo de estatística utilizado nativamente pelo Power BI.

-   **Estatística Inferencial:** utiliza técnicas e métodos para fazer generalizações e previsões a partir de dados amostrais, permitindo inferências sobre uma população maior. Envolve testes de hipóteses, intervalos de confiança e análise de regressão, entre outras técnicas. Para isso, geralmente são usadas outras ferramentas, como Python e R.

-   No dia a dia do Power BI, trabalha-se principalmente com tabelas e gráficos, medidas de tendência central, medidas de dispersão e medidas de posição.

-   Já na Estatística Inferencial entram conceitos como estimação, testes de hipóteses, análise de regressão, ANOVA e modelos de probabilidade.

Dados primários x dados secundários

-   **Dados primários:** referem-se à coleta de informações atuais, como pesquisas e questionários aplicados especificamente para o estudo.

-   **Dados secundários:** referem-se à coleta de informações que já estão disponíveis, como dados acadêmicos ou pesquisas já finalizadas.

Variável, observação e parâmetro

-   **Variável:** representação numérica de uma característica que está sendo medida ou observada.

-   **Observação:** representação de um componente específico do conjunto de dados, como uma pessoa, um objeto etc.

-   **Estatística:** no sentido técnico, refere-se ao ato de calcular medidas a partir de uma amostra.

-   **Parâmetro:** refere-se à compreensão de uma medida associada à população como um todo (e não apenas à amostra).

-   **Variável qualitativa:** descreve o componente, como pessoa, objeto ou país (categorias, não números).

-   **Variável quantitativa:** representa uma expressão numérica, como idade ou altura.

Medidas de posição (tendência central)

As medidas de posição, também conhecidas como medidas de tendência central, são valores que descrevem o centro de um conjunto de dados. As três mais comuns são a média, a mediana e a moda — cada uma oferece uma forma diferente de resumir a distribuição dos dados.

-   **Média:** soma de todos os valores de um conjunto de dados dividida pelo número total de valores. É a medida mais comum, mas pode ser distorcida por valores extremos (outliers).

-   **Mediana:** valor que separa um conjunto de dados ordenado em duas metades iguais. Se o total de valores é ímpar, é o valor do meio; se for par, é a média dos dois valores centrais. É menos sensível a outliers do que a média.

-   **Moda:** valor que ocorre com maior frequência no conjunto de dados. Pode não haver moda, haver uma (unimodal) ou várias (multimodal); é útil tanto para dados numéricos quanto categóricos.

Coeficiente de variação

O coeficiente de variação (CV) é especialmente útil para comparar a dispersão de dois ou mais conjuntos de dados que possuem escalas ou unidades de medida diferentes, permitindo identificar qual conjunto tem maior variabilidade relativa, independentemente da unidade.

> **CV = (Desvio Padrão / Média) × 100**

Big Data Analytics

Big Data Analytics é o processo de examinar, analisar e extrair informações valiosas de grandes conjuntos de dados (Big Data), caracterizados por grande volume, variedade e velocidade — o que os torna complexos de processar por métodos tradicionais.

Envolve o uso de técnicas avançadas, como aprendizado de máquina (Machine Learning), mineração de dados, processamento de linguagem natural (PLN) e análise de texto, além de ferramentas e tecnologias especializadas para lidar com a escala e a complexidade dos dados.

O objetivo é identificar padrões, tendências e correlações ocultas, permitindo decisões mais informadas, melhoria da eficiência operacional, identificação de novas oportunidades e vantagem competitiva. Em Big Data Analytics aplicam-se técnicas de Estatística Descritiva e Inferencial, com aplicações como:

-   Análise preditiva

-   Análise de sentimento

-   Detecção de fraude

-   Análise de risco

-   Recomendação personalizada

-   Otimização da cadeia de suprimentos

-   População e amostra: conceitos-base para qualquer análise estatística — a população é o conjunto total, e a amostra é o subconjunto efetivamente coletado e analisado.

## Capítulo 12 — Limpeza e Manutenção de Dados

A limpeza e a manutenção de dados são etapas fundamentais antes de qualquer análise ou construção de dashboard.

Principais etapas

-   Remoção de dados duplicados: eliminar registros duplicados que podem distorcer a análise.

-   Tratamento de valores ausentes: substituir, remover ou estimar valores ausentes, usando métodos como média, mediana, interpolação ou outros algoritmos.

-   Correção de erros de digitação e inconsistências: identificar e corrigir erros de formatação e padronização dos dados.

-   Conversão de tipos de dados: transformar variáveis em tipos apropriados (numérico, categórico ou textual).

-   Renomeação e reorganização de colunas: ajustar nomes para facilitar a compreensão e organizar conforme a necessidade da análise.

-   Filtragem e seleção de dados: extrair subconjuntos específicos com base em critérios pré-determinados.

-   Discretização e binning: converter variáveis contínuas em categorias ou agrupar dados em faixas específicas.

-   Normalização e padronização: ajustar a escala de valores numéricos para facilitar comparações e melhorar modelos de Machine Learning.

-   Transformação de variáveis: criar novas variáveis a partir de outras existentes, ou aplicar transformações matemáticas.

-   Detecção e tratamento de outliers: identificar e tratar valores extremos que possam afetar a análise.

-   Codificação de variáveis categóricas: converter categorias em formatos numéricos (one-hot ou ordinal) para uso em modelos de Machine Learning.

Essas etapas variam conforme o contexto e os objetivos da análise. As ferramentas utilizadas podem incluir linguagens como Python, R e SQL, além de softwares como Excel, Power BI ou Tableau.

> **💡 Dica:** *De 50% a 70% do tempo de elaboração de um dashboard é dedicado à manipulação e limpeza de dados.*

Análise exploratória e tratamento no Power Query

-   **Null:** valor nulo, ou seja, ausência de dado.

A Análise Exploratória serve para conhecer melhor os dados que serão usados no dashboard, buscando possíveis erros de digitação, valores ausentes, valores duplicados e outliers (valores extremos).

No Power Query é possível identificar esses problemas de formas específicas:

-   **Valores ausentes:** aparecem como categoria Null e podem ser filtrados diretamente na coluna.

-   **Valores duplicados:** podem ser tratados usando "Agrupar Por" na coluna correspondente, ou removidos selecionando a coluna e clicando em Excluir Linhas > Remover Valores Duplicados.

-   **Outliers:** basta filtrar a coluna e identificar os números extremos; a partir disso, toma-se uma decisão com justificativa (corrigir, substituir ou remover). O box plot é um ótimo gráfico para identificar outliers, mas não está disponível nativamente no Power BI Desktop.

Na prática:

-   Valores ausentes: normalmente aplica-se um filtro para não exibir esses valores no dashboard, já que podem indicar erro de digitação ou falta de preenchimento.

-   Valores outliers: identificar e analisar para decidir se serão corrigidos (substituindo o valor conforme a análise) ou removidos do dashboard.

> **🛠️ Prática aplicada no curso:** *Lab 4 — Limpeza e manipulação de dados de cadastro de clientes no Power BI.*

## Capítulo 13 — Manipulação de Dados com Power Query e Linguagem M

Engenharia de atributos no Power Query

Qualquer operação realizada no Power Query já gera automaticamente um código em Linguagem M, que pode ser visualizado e editado sem bagunçar a estrutura, através do Editor Avançado.

-   **Exibição de Qualidade da Coluna:** identifica valores ausentes; funciona como uma validação para verificar se os dados estão corretos.

-   **Distribuição de Colunas:** resumo visual dos dados, útil para organização e identificação de valores distintos em cada coluna.

-   **Editor Avançado:** permite tratar as informações via Linguagem M sem bagunçar a estrutura já construída.

Linguagem M x DAX

-   ETL básico em M: estruturas como each, if\...else.

-   **Pacote Table:** conjunto de funções úteis para tratar as informações; vale a pena se aprofundar em pacotes e funções específicas.

-   **Escala logarítmica:** usada para colocar valores na mesma escala, comum em contextos de Machine Learning.

-   **Linguagem M:** usada dentro do Power Query para manipulação de dados: limpeza, mesclagem de colunas ou linhas, conversão de tipos de texto, etc.

-   **Funções DAX:** usadas no modelo de dados para criação de colunas e medidas calculadas, com análises mais aprofundadas.

> **💡 Dica:** *Vale a pena explorar tanto funções como IF quanto variáveis como VAR e RETURN dentro do DAX.*
>
> **🛠️ Prática aplicada no curso:** *Lab 5 — Engenharia de atributos com Linguagem M no Power BI.*

## Capítulo 14 — Power BI e Banco de Dados

Sistemas Gerenciadores de Bancos de Dados (SGBDs) são softwares responsáveis por gerenciar e administrar bancos de dados. Eles fornecem ferramentas para criar, manter, manipular, proteger e otimizar o acesso aos dados armazenados, facilitando operações como inserção, atualização, exclusão e consulta.

Tipos de SGBDs

-   **SGBDs Relacionais:** gerenciam bancos de dados relacionais, onde os dados são organizados em tabelas e as relações são estabelecidas por chaves primárias e estrangeiras. Utilizam SQL como linguagem padrão. Exemplos: MySQL, PostgreSQL, Oracle e SQL Server.

-   **SGBDs NoSQL:** gerenciam bancos de dados não relacionais, sem o modelo tabular clássico; são escaláveis e distribuídos. Incluem bancos de documentos (MongoDB, Couchbase), bancos de colunas (Cassandra, HBase), bancos de grafos (Neo4j, OrientDB) e bancos de chave-valor (Redis).

Além do armazenamento e da recuperação de dados, os SGBDs também são responsáveis por controle de transações, consistência, integridade referencial, segurança, gerenciamento de acesso e otimização de consultas.

Conexão do Power BI com bancos de dados

-   Para conectar um banco de dados no Power BI, é necessário instalar o driver de conexão específico para cada banco, para que a conexão funcione corretamente.

-   **ODBC (Open Database Connectivity):** interface de programação de aplicativos (API) padrão que permite que aplicativos se conectem a diferentes SGBDs, independentemente do sistema operacional, linguagem de programação ou modelo de banco. Foi desenvolvida pela Microsoft no início dos anos 1990 e é amplamente usada para acessar bancos como Oracle, SQL Server, MySQL e PostgreSQL.

-   **SQLite:** banco de dados utilizado no projeto do curso; tecnicamente não é considerado um software SGBD completo, mas sim um banco de dados leve que estrutura as informações em tabelas usando a linguagem SQL.

-   A instalação de drivers é necessária para configurar corretamente a conexão a partir do sistema operacional.

-   Ao conectar o banco de dados no Power BI, é possível usar filtros para extrair apenas as colunas necessárias, através de Configurações Avançadas, digitando o comando SQL diretamente (SELECT, FROM, WHERE, AND, OR, etc.).

> **🛠️ Prática aplicada no curso:** *Lab 6 — Trabalhando com Power BI e banco de dados para extração e análise de dados.*

## Capítulo 15 — SQL Analytics

A linguagem SQL (Structured Query Language) é uma linguagem de programação de domínio específico projetada para gerenciar e manipular dados armazenados em Sistemas de Gerenciamento de Bancos de Dados Relacionais (SGBDs). Desenvolvida na década de 1970 pela IBM, tornou-se o padrão para interagir com bancos relacionais em todo o mundo.

A SQL oferece recursos para criar, modificar, consultar e controlar o acesso a dados armazenados em um banco relacional. É baseada no modelo relacional, que organiza os dados em tabelas compostas por linhas e colunas, permitindo analisar os relacionamentos entre elas.

Grupos de comandos SQL

-   **DDL (Data Definition Language):** permite criar, alterar e excluir estruturas de banco de dados, como tabelas, índices e restrições. Exemplos: CREATE, ALTER, DROP.

-   **DML (Data Manipulation Language):** usado para inserir, modificar, excluir e consultar dados armazenados nas tabelas. Exemplos: SELECT, INSERT, UPDATE, DELETE.

-   **DCL (Data Control Language):** fornece mecanismos para controlar o acesso aos dados e gerenciar privilégios de usuários. Exemplos: GRANT, REVOKE.

-   **TCL (Transaction Control Language):** controla as transações, garantindo a consistência e a integridade dos dados. Exemplos: COMMIT, ROLLBACK, SAVEPOINT.

No curso, o SQLite Studio é utilizado para manipular e executar queries sobre o banco de dados SQLite criado no capítulo anterior — para cada SGBD, existe uma ferramenta específica de manipulação.

Comandos e cláusulas essenciais

-   **SELECT:** seleciona a(s) coluna(s) específica(s). O asterisco (*) é o operador coringa, que retorna todas as colunas e linhas.

-   **FROM:** define de qual tabela as informações serão retiradas.

-   **LIMIT:** limita a quantidade de linhas retornadas.

-   **DISTINCT:** retorna valores distintos (únicos) de uma coluna.

-   **WHERE:** aplica o filtro na tabela, filtrando linhas — ex.: WHERE ano = 2014.

Operadores

-   **Operadores de comparação:** = (igual a); > (maior que); < (menor que); >= (maior ou igual a); <= (menor ou igual a); <> (diferente de).

-   **AND:** equivale ao "&"; retorna resultados apenas quando ambas as condições forem verdadeiras.

-   **OR:** equivale ao "||"; retorna o resultado mesmo quando apenas uma das condições for verdadeira.

-   **BETWEEN:** retorna valores dentro de um intervalo — por exemplo, entre 310 e 320.

-   **LIKE:** equivalente ao FIND do Power BI; permite buscar e retornar um caractere específico dentro da coluna. O símbolo "%" é o caractere coringa, usado para localizar o texto em qualquer posição (início, meio ou fim).

-   **IN:** permite buscar informações dentro de uma coluna, retornando apenas os valores especificados entre aspas simples.

-   **NOT:** exclui as informações especificadas entre aspas simples; pode ser combinada com outras funções.

-   **ORDER BY:** ordena a coluna (caracteres, números ou letras), de forma crescente ou decrescente.

-   **MIN, MAX, AVG, SUM e COUNT:** funções matemáticas para calcular, respectivamente, o valor mínimo, máximo, a média, a soma e a contagem.

-   **GROUP BY:** agrupa colunas e informações; aplica-se às colunas que não possuem funções de agregação.

-   **AS:** permite renomear uma coluna no resultado da consulta.

-   **ROUND:** arredonda as casas decimais de valores numéricos.

-   **JOIN:** realiza junções entre informações de tabelas diferentes, complementando a análise.

-   **INSERT:** insere novas informações no banco de dados.

-   **UPDATE:** atualiza registros já existentes no banco de dados.

-   **DELETE:** remove um registro do banco de dados.

SQL Analytics no Power BI

Após finalizar toda a manipulação de queries em SQL, a conexão com o Power BI é feita via conexão de banco de dados: basta executar a mesma query salva no banco na opção avançada de conexão do Power BI, retornando as informações já totalmente tratadas.

> **💡 Dica:** *Tomar muito cuidado para não puxar informações em excesso, sob risco de travar o banco de dados.*

## Capítulo 16 — Machine Learning para Segmentação de Clientes (Python)

Machine Learning (Aprendizado de Máquina) é uma área da Inteligência Artificial que se concentra no desenvolvimento de algoritmos e técnicas que permitem que os computadores aprendam a executar tarefas sem serem explicitamente programados para isso. O objetivo é desenvolver modelos capazes de identificar padrões, fazer previsões e tomar decisões com base nos dados fornecidos.

Categorias de aprendizado de máquina

-   **Aprendizado Supervisionado:** o algoritmo é treinado com um conjunto de dados rotulados (entradas e saídas conhecidas) e aprende a mapear as entradas nas saídas corretas. Exemplos: classificação de imagens e previsão de preços.

-   **Aprendizado Não Supervisionado:** o algoritmo é treinado com dados não rotulados, buscando encontrar padrões e estruturas subjacentes. Exemplos: agrupamento (clustering) e redução de dimensionalidade.

-   **Aprendizado por Reforço:** o algoritmo (agente) aprende a tomar decisões com base em recompensas e punições, interagindo com um ambiente para maximizar recompensas a longo prazo. Exemplos: jogos e robótica.

Machine Learning tem ampla gama de aplicações, da análise de dados e previsão até a automação e o desenvolvimento de sistemas de recomendação — sendo uma das atividades centrais em projetos de Data Science. Neste capítulo, o foco é o Aprendizado Não Supervisionado, aplicado à segmentação e classificação de clientes.

Fluxo de trabalho com Python e Jupyter Notebook

-   Utiliza-se Machine Learning junto com a linguagem Python, através da plataforma Jupyter Notebook.

-   Instala-se o Anaconda Python no desktop, um pacote voltado para esse tipo de análise em Python.

-   A partir do CMD, executa-se o caminho onde o Anaconda Python está instalado e, em seguida, o comando para abrir o Jupyter Notebook, que roda através do navegador (Chrome).

> **💡 Dica:** *Para utilizar Machine Learning de forma útil, a empresa precisa ter um histórico de dados consistente — é esse histórico que alimenta e sustenta o aprendizado do modelo.*

Etapas típicas de um projeto de Machine Learning

-   Definição do problema

-   Importação dos pacotes (via Anaconda Python e Jupyter Notebook)

-   Carregamento dos dados

-   Análise exploratória

-   Resumo dos dados

-   Pré-processamento

-   Construção do modelo de Machine Learning

> **📌 Complemento:** *No fundo, Machine Learning é matemática computacional aplicada por meio de comandos e algoritmos — cada etapa acima existe para garantir que os dados cheguem "limpos" e bem compreendidos até a fase de modelagem.*
>
> **🛠️ Prática aplicada no curso:** *Lab 7 — Machine Learning com Linguagem Python e Power BI dentro do Jupyter Notebook.*

## Capítulo 17 — Machine Learning para Detecção de Anomalias (R)

A linguagem R é voltada especificamente para análise estatística.

-   Para trabalhar com R é necessário baixar a linguagem R, o Rtools e o RStudio (IDE).

-   **R e Rtools:** correspondem à interpretação do software (o motor de execução da linguagem).

-   **RStudio:** é o ambiente de desenvolvimento (IDE) onde o código é escrito e executado.

Estado supervisionado x não supervisionado (detecção de anomalias)

-   **Estado supervisionado:** processo de etiquetagem, em que se identifica a regra a partir de dados históricos de entrada, adicionando uma nova coluna com os dados de saída.

-   **Estado não supervisionado:** envolve o uso de algoritmos matemáticos para identificar padrões nos dados (por exemplo, através de média e desvio padrão); tudo o que estiver fora do padrão esperado é contabilizado como anomalia.

Os scripts em R e em Python seguem uma lógica parecida: primeiro desenvolve-se o código no software de estúdio (RStudio ou Jupyter Notebook) e, depois, integra-se o resultado ao Power BI.

> **🛠️ Prática aplicada no curso:** *Lab 8 — Detecção de anomalias em transações financeiras com Linguagem R e Power BI.*

## Capítulo 18 — Inteligência Artificial e Análise de Séries Temporais

Neste capítulo o foco é a previsão sobre séries temporais: analisar o comportamento de uma métrica (por exemplo, produção) ao longo do tempo e gerar previsões, usando os recursos de IA disponíveis dentro do Power BI.

O fator principal em uma série temporal é o tempo (ano, mês, dia, semana etc.), e o determinante é o que ocorre ao longo desse tempo (por exemplo, o volume de produção).

-   **Medida rápida — média móvel:** permite analisar a média de uma métrica ao longo do tempo, em intervalos de dias, meses ou anos, suavizando variações pontuais.

-   **Forecast:** recurso do Power BI usado para gerar a previsão futura de médias, projetando a tendência da série temporal para os próximos períodos.

-   Também é possível aplicar detecção de anomalias em séries temporais, identificando pontos fora do padrão esperado ao longo do tempo.

> **🛠️ Prática aplicada no curso:** *Lab 9 — Engenharia de Produção com Power BI e IA, prevendo a produção industrial ao longo do tempo.*
