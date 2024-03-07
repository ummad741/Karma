from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from fastapi_users import fastapi_users, FastAPIUsers

from users.baseconfig import auth_backend
from users.schemas import UserCreate, UserRead
from users.manager import get_user_manager
from users.models import User

# local folders and files

app = FastAPI(
    title='Ecommerce'
)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.name}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"


@app.get('/test/{id}')
def test(id: int):
    return id


@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.get('/zor/')
async def qalesan():
    return {"zor": "zor"}
