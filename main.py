from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DocuMind backend is running"}

@app.get("/about")
def about():
    return {"project": "DocuMind"}