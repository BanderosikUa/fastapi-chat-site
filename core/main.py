from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from database.connection import DbContext
from core.settings import BASE_DIR

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory="static"), name='static')


def get_db():
    with DbContext() as db:
        yield db
