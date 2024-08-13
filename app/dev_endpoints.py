# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/dev")
async def read_root():
    return {"message": "Hello World for dev"}

@app.get("/dev-test")
async def read_root():
    return {"message": "This is a test for dev"}
