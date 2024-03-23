import uvicorn
from pyrepositories import DataSource, JsonTable
import os
import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(os.path.join(path_root))

from app.lib import init_project, bootstrap
from app.models import Event, Organizer

def main():
    """Main entry point of the application."""

    # NOTE: Initialize the project
    data_dir = init_project()
    data_source = DataSource()

    # NOTE: Create the tables
    events_table = JsonTable("events", data_dir)
    organizers_table = JsonTable("organizers", data_dir)

    # NOTE: Add the tables to the data source
    data_source.add_table(events_table)
    data_source.add_table(organizers_table)
    
    # NOTE: Bootstrap the CRUDApi
    api = bootstrap(data_source)
    
    # NOTE: Get the FastAPI app from the api
    app = api.get_app()

    # NOTE: You can **register** a CRUD router: it won't get included in the app until you call `publish` on the api
    # Useful when you want to add custom routes to the router before including it in the app
    event_router = api.register_router('events', Event)

    # NOTE: Get the internal router to add custom routes
    event_base = event_router.get_base()

    @event_base.get("/events/{event_id}/attendees")
    async def get_event_attendees(event_id: int):
        return {"event_id": event_id, "attendees": ["Alice", "Bob", "Charlie"]}

    @event_base.post("/events/{event_id}/organizers")
    async def add_organizer(event_id: int, organizer_id: int):
        return {"event_id": event_id, "organizer_id": organizer_id}
    
    # NOTE: You can also **include** a CRUD router: it will be included in the app immediately
    # Useful when you don't need to add custom routes to the router
    api.include_router('organizers', Organizer)

    # NOTE: Register the custom routers
    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    # NOTE: Publish the CRUD routers before running the app
    # It won't harm anything, because the routers check if they are already included in the app
    api.publish()

    uvicorn.run(app, host="0.0.0.0", port=1234)

if __name__ == "__main__":
    main()

