
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

SERVICE = "post-app"

@app.get("/posts")
def read_posts():
    return JSONResponse(
        content={
            "title": "post api",
            "articles": [
                {"num": 77, "title": "감격", "writer": "수강생B"},
                {"num": 78, "title": "질문", "writer": "주니어"}
            ]
        },
        media_type="application/json; charset=utf-8"
    )
    

@app.get("/health")
def health():
    return {"service": SERVICE, "message":"market service is running"}