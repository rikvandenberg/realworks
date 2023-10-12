import os
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/config/")
def read_config():
    return {"message": os.getenv('MESSAGE')} 