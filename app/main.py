# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/test")
async def read_root():
    return {"message": "This is a test"}

@app.get("/about")
async def read_root():
    return {"message": "About endpoint"}


@app.get("/add/{a}/{b}")
async def add(a: int, b: int):
    return {"result": a + b}