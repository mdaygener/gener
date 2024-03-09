    zfrom fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/add/{num1}/{num2}")
async def add_numbers(num1: float, num2: float):
    return num1 + num2

@app.get("/subtract/{num1}/{num2}")
async def subtract_numbers(num1: float, num2: float):
    return num1 - num2

@app.get("/multiply/{num1}/{num2}")
async def multiply_numbers(num1: float, num2: float):
    return num1 * num2

@app.get("/divide/{num1}/{num2}")
async def divide_numbers(num1: float, num2: float):
    if num2 == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return num1 / num2