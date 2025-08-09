# Your FastAPI backend main.py
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello from MS Surveyor!'}
