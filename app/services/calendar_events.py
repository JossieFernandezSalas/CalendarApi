# Author: Jossie Esteban Fernández Salas
# Email: jossie.fernandez.salas@gmail.com
# Linkedin: linkedin.com/in/jossiefernandez

from app.responses.response import response_json
from app.services.calendar_services import get_calendar_service


service = get_calendar_service()


def create_event(template: dict):
    try:
        response = service.events().insert(calendarId="primary", body=template).execute()
        return response
    except Exception as e:
        return response_json(message=e.message, status=500)


def get_events():
    try:
        response = service.events().list(calendarId="primary",
                                         maxResults=200,
                                         singleEvents=True,
                                         orderBy="startTime",
                                         showDeleted=False,
                                         showHiddenInvitations=False,
                                         timeMin="2023-01-01T01:00:00Z",
                                         timeMax="2023-12-31T23:59:00Z").execute()
        return response["items"]
    except Exception as e:
        return response_json(message=e.message, status=500)


def get_event(eventId: str):
    try:
        response = service.events().get(calendarId="primary", eventId=eventId).execute()
        return response
    except Exception as e:
        return response_json(message=e.message, status=500)


def delete_event(eventId: str):
    try:
        response = service.events().delete(calendarId="primary", eventId=eventId).execute()
        return response
    except Exception as e:
        return response_json(message=e.message, status=500)


def update_event(eventId: str, template: dict):
    try:
        response = service.events().update(calendarId='primary', eventId=eventId, body=template).execute()
        return response
    except Exception as e:
        return response_json(message=e.message, status=500)