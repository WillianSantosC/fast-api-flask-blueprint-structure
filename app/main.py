from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import routers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

routers.init_routes(app)
