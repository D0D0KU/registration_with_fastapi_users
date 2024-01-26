import uvicorn as uvicorn

from fastapi import FastAPI

from src.auth.router import router_auth, router_register


app = FastAPI()
app.include_router(router_auth)
app.include_router(router_register)


if __name__ == "__main__":
    uvicorn.run(app=app)
