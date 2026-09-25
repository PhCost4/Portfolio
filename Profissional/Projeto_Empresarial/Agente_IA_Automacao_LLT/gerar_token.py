from google_auth_oauthlib.flow import InstalledAppFlow
import json

SCOPES = [
  'https://www.googleapis.com/auth/spreadsheets.readonly',
  'https://www.googleapis.com/auth/drive.readonly'
]

# Abre navegador para autorizar — só roda uma vez
flow = InstalledAppFlow.from_client_secrets_file(
  'credentialsOutput.json', SCOPES)
creds = flow.run_local_server(port=0)

# Exibe o token para copiar no GitHub Secrets
print("=== COPIE TUDO ABAIXO PARA O SECRET GOOGLE_TOKEN ===")
print(creds.to_json())