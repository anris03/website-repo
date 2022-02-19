from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        # request_body={
        #     'summary':'test_cal'
        # }

        # response=service.calendars().insert(body=request_body).execute()
        # print(response)

        # event = {
        #         'summary': 'test1_event',
        #         'description': 'A chance to hear more about Google\'s developer products.',
        #         'start': {
        #             'dateTime': '2022-02-21T09:00:00',
        #             'timeZone': 'Asia/Kolkata',
        #         },
        #         'end': {
        #             'dateTime': '2022-02-21T09:45:00',
        #             'timeZone': 'Asia/Kolkata',
        #         },
        # }
        # event = service.events().insert(calendarId='oq6jav7vmlfv2uj91vh1lmupvc@group.calendar.google.com', body=event).execute()
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='oq6jav7vmlfv2uj91vh1lmupvc@group.calendar.google.com', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()




# from __future__ import print_function

# import datetime
# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',
#           'https://www.googleapis.com/auth/calendar',
#           'https://www.googleapis.com/auth/calendar.events',
#           'https://www.googleapis.com/auth/calendar.events.readonly'
# ]


# def main():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     try:
#         service = build('calendar', 'v3', credentials=creds)
#         # request_body={
#         #     'summary':'test_cal'
#         # }

#         # response=service.calendars().insert(body=request_body).execute()
#         # print(response)

#         # event = {
#         #         'summary': 'test1_event',
#         #         'description': 'A chance to hear more about Google\'s developer products.',
#         #         'start': {
#         #             'dateTime': '2022-02-20T09:00:00',
#         #             'timeZone': 'Asia/Kolkata',
#         #         },
#         #         'end': {
#         #             'dateTime': '2022-02-20T09:45:00',
#         #             'timeZone': 'Asia/Kolkata',
#         #         },
#         # }
#         # event = service.events().insert(calendarId='oq6jav7vmlfv2uj91vh1lmupvc@group.calendar.google.com', body=event).execute()
#         # # Call the Calendar API
#         now = datetime.datetime.utcnow().isoformat() #+ 'Z'  # 'Z' indicates UTC time now(pytz.timezone('Asia/Kolkata'))
#         print('Getting the upcoming 10 events')
#         events_result = service.events().list(calendarId='oq6jav7vmlfv2uj91vh1lmupvc@group.calendar.google.com', timeMin=now,
#                                               maxResults=10, singleEvents=True,
#                                               orderBy='startTime').execute()
#         events = events_result.get('items', [])
#         print(dir(service)) #*********************************

#         if not events:
#             print('No upcoming events found.')
#             return

#         # Prints the start and name of the next 10 events
#         for event in events:
#             print(event,"******")
#             start = event['start'].get('dateTime', event['start'].get('date'))
#             print(start, event['summary'])

#     except HttpError as error:
#         print('An error occurred: %s' % error)


# if __name__ == '__main__':
#     main()