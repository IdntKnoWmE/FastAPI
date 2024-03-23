# user imports
from models.note import Note
from config.db import mydb_conn
from schema.note import note_instance, notes_instance

# default imports
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi import Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# templates folder created and jinja is pointed towards that
templates = Jinja2Templates(directory="templates")

# Creating a router for the APIs
note_router = APIRouter()


@note_router.get('/', response_class=HTMLResponse)  # GET request for hitting localhost/
async def read_item(request: Request):
    data = notes_instance(mydb_conn.notes.find({}))

    return templates.TemplateResponse("index.html", {"request": request, "data": data,
                                                     "message": request.query_params.get("message")})


@note_router.post("/submit", response_class=RedirectResponse)
async def add_note(request: Request):
    form = await request.form()
    form_dict = dict(form)
    valid_note = Note(title=form_dict["title"], description=form_dict["description"],
                      important=form_dict.get("important", False))

    # insert data into mongo
    mydb_conn.notes.insert_one(valid_note.model_dump())

    # Redirect to the home page with a success message
    return RedirectResponse(url="/", status_code=303)


@note_router.get('/items/{item_id}')
def read_item(item_id: int, q: list | str = []):
    # With the use of list | str, the function will consider q as either list or string anf based on that
    # it will show you the suggestive methods used with q once you type '.' After q. This is known as
    # Typing in Python.
    return {'item:id': item_id, 'type': str(type(item_id)), 'q': q}
