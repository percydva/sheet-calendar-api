import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import timedelta
from dateutil import parser

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/calendar'
]
SPREADSHEET_ID = '1ccUONazS8vIYbgwO8SDTmpF6J0Oa71ezaafZqHrf7s8'
CALENDAR_ID = 'toouynchan@gmail.com'
SHEET_NAME = 'Hongkong'

def get_events(calendar_id, calendar_service, data):
    for row in data:
        title, atd, etd = row.get('Lô hàng'), row.get('ATD'), row.get('ETD')
        if not atd and not etd:
            print(f'Skipping row with missing ATD and ETD: {row}')
            continue
        date_source = 'ATD' if atd else 'ETD'
        date_str = atd if atd else etd

        try: 
            event_date = parser.parse(date_str).date()
        except Exception as e:
            print(f"Error parsing date '{date_str}' for row {row}: {e}")
            continue
        
        event_summary = f'{title} {date_source}'
        event = {
            'summary': event_summary,
            'start': {
                'date': str(event_date)
            },
            'end': {
                'date': str(event_date+timedelta(days=1))
            },
        }

        try:
            calendar_service.events().insert(calendarId=calendar_id, body=event).execute()
            print(f'Event created: {event_summary} on {event_date}')
        except Exception as e:
            print(f"Error creating event '{row}': {e}")

def delete_all_events(calendar_service, calendar_id):
    print("Fetching all events...")
    events_result = calendar_service.events().list(
        calendarId=calendar_id,
        timeMin='2000-01-01T00:00:00Z',  # Include past events
        maxResults=2500,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    deleted = 0

    for event in events:
        calendar_service.events().delete(calendarId=calendar_id, eventId=event['id']).execute()
        deleted += 1

    print(f"Deleted {deleted} events from calendar: {calendar_id}")

def main():
    creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
    gc = gspread.authorize(creds)
    calendar_service = build('calendar', 'v3', credentials=creds)
    spreadsheet = gc.open_by_key(SPREADSHEET_ID)
    worksheet = spreadsheet.worksheet(SHEET_NAME)
    data = worksheet.get_all_records(head=2)
    delete_all_events(calendar_service, CALENDAR_ID)
    get_events(CALENDAR_ID, calendar_service, data)

if __name__ == '__main__':
    main()