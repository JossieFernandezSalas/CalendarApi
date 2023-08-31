from fastapi import APIRouter, Request
from app.services.calendar_events import create_event, get_event, delete_event, update_event


calendar_routes = APIRouter()


@calendar_routes.post("/create")
async def create(request: Request):
    template = await request.json()
    return create_event(template)




@calendar_routes.get("/event/{eventId}")
def get(eventId: str):
    return get_event(eventId)


@calendar_routes.delete("/delete/{eventId}")
def delete(eventId: str):
    return delete_event(eventId)


@calendar_routes.put("/update/{eventId}")
async def put(request: Request, eventId: str):
    template = await request.json()
    return update_event(eventId,template)