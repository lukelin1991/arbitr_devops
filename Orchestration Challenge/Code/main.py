from fastapi import FastAPI
from APIs import TestAPIs

app = FastAPI()
api_handler = TestAPIs()
app.include_router(api_handler.router)