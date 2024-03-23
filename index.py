from fastapi import FastAPI
from routes.note import note_router
from fastapi.staticfiles import StaticFiles

# app creation
app = FastAPI()  # To start, the fast api server use 'uvicorn index:app --reload'

# Static folder mount for images, audio, css and video
app.mount("/static", StaticFiles(directory="static"), name="static")

# include routers in the app
app.include_router(note_router)
