import gspread
from google.oauth2.service_account import Credentials
import requests
import pandas as pd

# Configurações para autenticação com Google Sheets
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

# Credenciais manuais
creds = {
    "type": "service_account",
    "project_id": "braboapp-428314",
    "private_key_id": "74dd23c0c3b1a95ff89b3a38fff18256f46dc988",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQClCcjmkQfVf6PZ\nA0pjzJY2laySC7UyKNINzPn1P02FkywEHFDyIHeM2k/2k+PAbQq2orAFTjcQPVK6\nVlDTb8+JVXf8H8dTbCjizd3ewXWMc+HC2Z6mHEXMz7jM8PnseddJsv591yWKKin6\nx5aeFLfFDoJKUKk/V9La2fjeqZclFPtueX45EbyLmWCl5zOyGxFSDNIjFyPamp9y\nw8XoXAhjDBzISGeFZDi+N2g+cc0+RGxeC7ipzxJ4sN+Zsdxy1RUQAM2lxQ4B3vKv\n0i1Q0XvKbkO2MsLiWNeOymQJvwGdLACnTPEW29R7fTVQ/6/SKDekSlz/9pDBGQSz\nfaNW6zkbAgMBAAECggEAFhNKe54aTvz9RMmzZB5ZWLYe41l3ObKLHPcg13n0W8cf\n+UbJBFzCZk/3UoiyoKpqkfEN8WURFCDXwClL3hRTzXoQtrk7d2r9cbpOu1KORM9l\nUHkSca6mHtYJe+RJ0c9JtEfMfGGlrvxNKYhpRajeHJjVuwIHZCZ9A51qCW05fzyU\nLpLf+ErqH/pHu1yOldNAR/2vvORZCLjWp2qHCfgJTNkzHZg27tSg0r9wF55KqUjE\nQMe28pLeXOih0DBpBKPWN0UeWcUKaC0SJkfwyzyhX4J5GtGrdjmDEiBMog7CRDdG\ntaBLuHpADLt1Dnobxo0ZkHfUT+E128+605GWBLvEcQKBgQDiBd0jgaX6sW9swLre\nkEqnMWc8lAV4nkOpD0PKXTM4MjTpzdL0drLW5r5rVbup8Kb+GbW1yrzJo708gwf+\nmJ8NXQibH0gRlq6vCOv2norUn8F4OY09CKynKC+wwQIPmq+lQMXpDpVh9Yfa+d7S\n5bX8vdArnLenYJH+onu+9cRB0QKBgQC67VAw8PlbLUxjCxNJmas04050ZrZruzi2\nKdZ6l5fJh+yt21VJRC0/dWQVRwbMdd5pXoICR2U7rqvdHtf47pggtp/v25RqmdJh\nkLFGnJ/A6jpg2QmVkI7u9k/mBiN0I8ztCiXcvEjTnVmW2ey0HgM0t4vI1srYqZda\nntNTOHk7KwKBgQDfYnRBF23360346jLGrU1bGRSzZohRwfmVKSUS6DIrJFPvkCEi\nw/3VL5CbfMxRFSu2j6pr1cfochAhsk9AbY8lIgHTboNH/uj+zY6I3ADSTGJmdFsH\nK3+YZbtcsiVbTsKyTOZNhMBXZNe0sKhtP+MxvFf2Apnwrx0b0XMENNqXQQKBgHYY\nD52b4C2WRLgd+yV4jA1xvdMUQRN2yLFtZS82LpMH6KM9+ne7Nsrsozo+ETGDFeyD\n5KcD7BT0mWetYMzIEBw6xHiIxQ9D9wHko9r0gIkkcZVWCRQQq/yUaI3uOt/Y7lKj\nIqB945StyDfhngV9IJFhlFJiQOz418JMrT3aY9zZAoGBAKvvm+8sDtUrBT2Avm2T\n0OPjf2/o54+9mq7M7nwIk0V5uUbEhLefeIQik8b+3q7e7CAXqZAMDpQVTMkjJ9Ti\n5i763+za+aTa12kDxQvKvgmBOK8RHWZq0P6tvQBPCGDLrJmCs/B4VnGn7HwqEKkd\nEVpr+1FTuvbWxZPH65oVYdYc\n-----END PRIVATE KEY-----\n",
    "client_email": "braboresults@braboapp-428314.iam.gserviceaccount.com",
    "client_id": "260441129869-2h170rfg25fo1ht9cpub2jvflabgp7ie.apps.googleusercontent.com",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-client-email%40your-project-id.iam.gserviceaccount.com"
}

# Converta as credenciais para um objeto Credentials
credentials = Credentials.from_service_account_info(creds, scopes=scope)
client = gspread.authorize(credentials)

# Função para buscar dados da URL e atualizar o Google Sheet
def update_sheet():
    url = "https://api.brabocar.com.br/api/manager/report/23d2721d-93ca-48c9-995d-e66beef250ab/2024-07-01/2030-12-31"
    response = requests.get(url)
    data = response.json()
    
    # Supondo que os dados sejam uma lista de dicionários
    df = pd.DataFrame(data)
    
    # Acesse a planilha e a aba onde os dados serão escritos
    spreadsheet = client.open("Dados Vendas API")
    sheet = spreadsheet.worksheet("Sheet1")
    
    # Apague os dados existentes na aba
    sheet.clear()
    
    # Escreva os dados atualizados na aba
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

# Executar a função de atualização uma vez
update_sheet()
