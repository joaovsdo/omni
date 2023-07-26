from __future__ import print_function

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

class InvalidTokenError(Exception):
    pass

def validaToken():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    path_token='/home/joaovsdo/.ssh/token.json'
    path_creds='/home/joaovsdo/.ssh/credentials.json'
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(path_token):
        creds = Credentials.from_authorized_user_file(path_token, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                path_creds, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(path_token, 'w') as token:
            token.write(creds.to_json())
    # Check if the token is still not valid after attempting to refresh
    if not creds or not creds.valid:
        raise InvalidTokenError("The token is invalid or expired. Please reauthorize the application.")

try:
    validaToken()
    # Call other functions that require valid credentials
    # For example: values = read_data_from_spreadsheet()
except InvalidTokenError as e:
    print("Warning:", e)
    # Take appropriate actions, e.g., exit the program or prompt the user to reauthorize.
except HttpError as e:
    print("An HTTP error occurred:", e)
    # Handle other potential errors with the API calls here
