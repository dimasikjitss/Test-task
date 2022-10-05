# from googleapiclient.discovery import build
# from google.oauth2 import service_account
# import pandas as pd
# import requests
# import psycopg2
# from sqlalchemy import create_engine
#
#
# def build_service(SAMPLE_SPREADSHEET_ID):
#     SERVICE_ACCOUNT_FILE = 'keys.json'
#     SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#     creds = None
#     creds = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#     service = build('sheets', 'v4', credentials=creds)
#     data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
#     current = data['Valute']['USD']['Previous']
#     # Call the Sheets API
#     sheet = service.spreadsheets()
#     result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="sales").execute()
#     values = result.get('values', [])
#
#     df = pd.DataFrame(values[1::])
#     df.insert(4, "4", [int(i) * current for i in df[2]])
#     df.columns = values[0] + ['стоимость,руб']
#     print(df)
#     engine = create_engine('postgresql://dimasik:password@localhost:5432/dimasik')
#     df.to_sql('tests2', engine, index=False, if_exists='replace')
#
#
# build_service('1-8_ueWU39bfm3K88USZU205A2PIBJkinjmF-7ouoODU')
