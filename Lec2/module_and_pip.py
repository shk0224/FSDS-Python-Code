from typing import Union

from fastapi import FastAPI
from uvicorn import run as app_run

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World, I am boss"}

if __name__ == "__main__":
    app_run(app, host='0.0.0.0', port=8080)