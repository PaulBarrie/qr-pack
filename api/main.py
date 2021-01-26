from fastapi import FastAPI

app = FastAPI()


@app.post("/graphql")
def read_root():
    return {"Hello": "World"}



