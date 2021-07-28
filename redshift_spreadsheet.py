import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from sqlalchemy import create_engine
from df2gspread import df2gspread as d2g

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]


def write_googlesheet(df, spreadsheet_key, sheet_title, starting_cell, overwrite):
    d2g.upload(df, spreadsheet_key, sheet_title, credentials=credentials, col_names=overwrite, row_names=True, start_cell = starting_cell, clean=overwrite)


if __name__ == "__main__":

    engine = create_engine('postgresql://frenny:BWhKx79Beyna4tLG@redshift-cluster-1.czcigf1qnvhe.eu-central-1.redshift.amazonaws.com:5439/dwh')
    data_frame = pd.read_sql('SELECT * FROM tgt_dev.purchase_prod;', engine)
    print(data_frame)
    credentials = ServiceAccountCredentials.from_json_keyfile_name('test-rebike-ca858a6200ac.json', scope)
    client = gspread.authorize(credentials)
    write_googlesheet(data_frame, '1MogvCK7mTPYv2Mmeapyq_D3hnOvlSynfUyADEBpL3F8', 'Sheet1', 'A1', True)
