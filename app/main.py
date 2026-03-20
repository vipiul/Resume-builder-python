from fastapi import FastAPI
from app.db.client import init_db
from app.api.v1 import auth
from app.api.v1 import resume

app = FastAPI(title="FastAPI Large App")

# @app.on_event("startup")
# async def on_start():
#     await init_db()


# app.include_router(auth.router, prefix="/api/v1")
app.include_router(resume.router, prefix="/api/v1")


@app.get("/health")
async def health():
    return {"status": "ok"}