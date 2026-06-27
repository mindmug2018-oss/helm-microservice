# main.py (for fastapi-market)
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/market")
def read_market():
    return JSONResponse(
        content={
            "title": "market api",
            "products": [
                {"id": 1, "name": "아이폰", "price": "품절"},
                {"id": 2, "name": "안드로이드", "price": "0원"}
            ]
        },
        media_type="application/json; charset=utf-8"
    )