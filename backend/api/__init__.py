from fastapi import FastAPI

from models import engine


app = FastAPI()

from . import routes
