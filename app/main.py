from fastapi import FastAPI
from app.routes import calendar
from app.services import calendar_services

app = FastAPI()
app.include_router(calendar.calendar_routes, prefix="/calendar")

calendar_services.get_calendar_service()