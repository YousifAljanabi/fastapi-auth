import uuid
from fastapi import FastAPI, Depends
from db import create_db_and_tables, get_user_db
from asyncio import create_task
from fastapi_users import FastAPIUsers, models
from backends import JWT_Bearer_backend, JWT_Cookie_backend
from users import User
from backends import auth_backends
from users import get_user_manager
from schemas import UserRead, UserCreate, UserUpdate

create_task(create_db_and_tables())
app = FastAPI()


fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, auth_backends)
current_active_user = fastapi_users.current_user(active=True)

app.include_router(
    fastapi_users.get_auth_router(JWT_Bearer_backend), prefix="/auth/jwt_bearer", tags=["auth_bearer"]
)

app.include_router(
    fastapi_users.get_auth_router(JWT_Cookie_backend), prefix="/auth/jwt_cookie", tags=["auth_cookie"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


