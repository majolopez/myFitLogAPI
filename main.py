from fastapi import FastAPI

app = FastAPI(title="Hello World API")

@app.get("/hello")
def hello_world():

    return {
        "status": "ok",
        "message": "Hello World"
    }
