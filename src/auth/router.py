from fastapi import HTTPException, Request, status, Depends
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy import select, update

from src.auth.models import User, get_async_session
from src.auth.auth_backend import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schemas import UserCreate, UserRead
from src.auth.castom_fau.email import very_token
from src.auth.castom_fau.fastapi_users import FastAPIUsers

from requests import Session


templates = Jinja2Templates(directory='src/templates')

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


router_auth = APIRouter(prefix="/auth/jwt", tags=["auth"])
router_auth.include_router(fastapi_users.get_auth_router(auth_backend))

router_register = APIRouter(prefix="/auth", tags=["auth"])
router_register.include_router(fastapi_users.get_register_router(UserRead, UserCreate))


@router_auth.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router_register.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router_auth.get("/verification")
async def verification(request: Request, token: str, session: Session = Depends(get_async_session)):

    payload = very_token(token=token)

    async with session as conn:
        very_user = await conn.execute(
            select(User.id)
            .where(User.id == payload['id'], User.username == payload['username'])
        )

        very_user = very_user.all()
        
    if very_user:
        async with session as conn:
            await conn.execute(update(User).where(User.id == payload['id']).values(is_verified=True))
            await conn.commit()

        return 'User verified!'

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid token or expired token"
                        )


@router_register.get("/registration-success", response_class=HTMLResponse)
async def registration_success(request: Request):
    return templates.TemplateResponse("registration_success.html", {"request": request})


@router_auth.get("/dashboard", response_class=HTMLResponse)
async def registration_success(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
