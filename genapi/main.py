from genapi.models.base_model import BasicPost

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "suh dude"}

@app.post("gen/py/{user_id}/question")
async def echo(question: BasicPost, user_id: str):
    return "User " + user_id + " asks: " + question.value
