import uvicorn as uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.auth.router import router_auth, router_register


app = FastAPI()
app.include_router(router_auth)
app.include_router(router_register)

app.mount("/static", StaticFiles(directory="src/static"), name="static")


if __name__ == "__main__":
    uvicorn.run(app=app)
