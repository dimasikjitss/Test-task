from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import requests
from sqlalchemy import create_engine
from config import *
import threading
import time


def build_service():
    # Connect to Sheets API
    cred = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=cred)
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="sales").execute()
    values = result.get('values', [])

    return values


def write_to_db(values):
    # Get current rate from CBR (USD)
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    current = data['Valute']['USD']['Previous']
    # Data preparation
    df = pd.DataFrame(values[1::])
    df.insert(4, "4", [int(i) * current for i in df[2]])
    df.columns = values[0] + ['стоимость,руб']
    # Create and writing data in Data Base
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

    df.to_sql('tests2', engine, index=False, if_exists='replace')


def main():
    while True:
        write_to_db(build_service())
        time.sleep(2)


if __name__ == '__main__':
    thr = threading.Thread(target=main)
    thr.start()
