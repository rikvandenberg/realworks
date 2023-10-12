import os
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/configs")
def read_configs():
    response = {}
    for name, value in os.environ.items():
        response[name] = value
    return response
    


@app.get("/configs/message")
def read_config():
    return {"message": os.getenv('MESSAGE')} 

