from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def read_main(token: str = None):
    if token != "gener":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "Hello, World!"}
