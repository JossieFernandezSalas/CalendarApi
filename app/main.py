# Author: Jossie Esteban Fernández Salas
# Email: jossie.fernandez.salas@gmail.com
# Linkedin: linkedin.com/in/jossiefernandez

from fastapi import FastAPI
from app.routes import calendar
from app.services import calendar_services
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(calendar.calendar_routes, prefix="/calendar")


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

calendar_services.get_calendar_service()
