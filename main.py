from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Service is Running!"}


@app.get("/healthcheck", status_code=200)
def healthcheck():

    varenvs = [
        "VAR_ONE",
        "VAR_TWO"
    ]
    return {"varenv": "OK", "database": "OK"}
