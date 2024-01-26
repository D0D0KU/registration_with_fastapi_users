from fastapi.routing import APIRouter

from fastapi_users import FastAPIUsers

from src.auth.models import User
from src.auth.auth_backend import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schemas import UserCreate, UserRead


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router_auth = APIRouter(prefix="/auth/jwt", tags=["auth"])
router_auth.include_router(fastapi_users.get_auth_router(auth_backend))

router_register = APIRouter(prefix="/auth", tags=["auth"])
router_register.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
