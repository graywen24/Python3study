from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pandas as pd
import numpy as np
import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from df2gspread import gspread2df as g2d  #download
from df2gspread import df2gspread as d2g   #upload

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SAMPLE_SPREADSHEET_ID = '1VmTci9v_A4fIlqhmdx_xAW-4pSLUjQ_KbhIugN4xcys'
SAMPLE_RANGE_NAME = 'sheet2'
creds = ServiceAccountCredentials.from_json_keyfile_name('sa.json',scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])
print(values)



# Opening JSON file
print(os. getcwd())


def Export_Data_To_Sheets():
    f = open('instanceSettoJson.json', )
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    print(type(data))   #list
    #df = pd.read_json(data)
    for i in range(len(data)):
        for x in range(len(data[i]['PrivateIpAddresses'])):
            print(data[i]['PrivateIpAddresses'][x])   #list->dict->ip is a list-->str
        for y in range(len(data[i]['PublicIpAddresses'])):
            print(data[i]['PublicIpAddresses'][y])

        print(data[i]['VirtualPrivateCloud']['VpcId'])
    res = pd.json_normalize(data)
    #print(res)

    df = pd.DataFrame(res)
    #d2g.upload(df, gfile=SAMPLE_SPREADSHEET_ID,clean=True, credentials=creds,row_names=False)
    f.close()


Export_Data_To_Sheets()