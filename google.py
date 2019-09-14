from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
spreadsheet_id = '1d2XvYZyG0K8GAv5bwakrzJsDWAR5Z7poKGIA2Guko3M'
range_name = 'A:Z'  # full range

def main():
    """Reads values from a spreadsheet
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                range=range_name).execute()
    values = result.get('values', [])
    print(values)

    if not values:
        print('No data found.')

    # title = 'test'
    # spreadsheet = {
    # 'properties': {
    #     'title': title
    #     }
    # }
    # spreadsheet = service.spreadsheets().create(body=spreadsheet,
    #                                     fields='spreadsheetId').execute()
    # print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))

if __name__ == '__main__':
    main()