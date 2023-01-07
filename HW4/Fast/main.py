from fastapi import FastAPI
from routes.routes import pord_api_router

tags_metadata = [
    {
        "name": "basic",
        "description": "classic search by id function",
    },    
    {
        "name": "function with name",
        "description": "search by name function",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

app.include_router(pord_api_router)
