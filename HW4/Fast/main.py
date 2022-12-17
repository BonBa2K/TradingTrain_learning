from fastapi import FastAPI
from routes.pords_routes import pord_api_router
app = FastAPI()

app.include_router(pord_api_router)
