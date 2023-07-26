from __future__ import print_function

import os.path

from warnings_email import geraWarning
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SAMPLE_SPREADSHEET_ID = "1IbOC2ujcYgfc8PRO86_x_9vjKxkegic7-_-zPuYLZ8E"
SAMPLE_RANGE_NAME = 'Base!A2:E'

HEADERS_SPREADSHEET_ID = "1boNUzGAX0cGxAWPcXVRsRtwYt611ohBqOnmkeIg6qFE"

def getCreds():
    creds=None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
           geraWarning('Credenciais expiradas')

    return creds

def updateValues(linha , values):
    """
        Creates the batch_update the user has access to.
        Load pre-authorized user credentials from the environment.
        TODO(developer) - See https://developers.google.com/identity
        for guides on implementing OAuth2 for the application.
            """
    
    
    creds = getCreds()
    # pylint: disable=maybe-no-member
    try:
        service = build('sheets', 'v4', credentials=creds)
        clearValues()
        result = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                        range=f"A2:I{linha}", 
                                                        valueInputOption="USER_ENTERED", 
                                                        body={"values": values}).execute()
        print(f"{(result.get('updatedCells'))} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def clearValues():
    
    creds = getCreds()
    service = build('sheets', 'v4', credentials=creds)

    header_range = 'Base!1:1'
    header_data = service.spreadsheets().values().get(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range=header_range).execute().get('values', [])
    

    # Limpar todas as linhas exceto a primeira
    requests = [{
    'updateCells': {
        'range': {
            'sheetId': 0  # ID da folha (0 para a primeira folha, 1 para a segunda, etc.)
        },
        'fields': 'userEnteredValue'
        }
    }]

    body = {
    'requests': requests
    }
    response = service.spreadsheets().batchUpdate(
    spreadsheetId=SAMPLE_SPREADSHEET_ID,
    body=body).execute()

    # Adicionar novamente o cabeçalho à primeira linha
    if header_data:
        header_values = header_data[0]
        header_range = 'Base!1:1'
        body = {
            'values': [header_values],
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range=header_range,
            valueInputOption='RAW', body=body).execute()
        
        
def getHeaders() -> list:
    creds = getCreds()
    service = build('sheets', 'v4', credentials=creds)

    header_range = 'Base!A1:A29'
    header_data = service.spreadsheets().values().get(
    spreadsheetId=HEADERS_SPREADSHEET_ID, range=header_range).execute().get('values', [])
    return header_data
