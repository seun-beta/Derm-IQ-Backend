from fastapi import FastAPI


app = FastAPI()


@app.get("/", tags=["root"])
def root():
    return {"data": "welcome home!"}
