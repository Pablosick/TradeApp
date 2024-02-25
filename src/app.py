import uvicorn
from fastapi import FastAPI

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate


app = FastAPI(title="Trading_app")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)  # Авторизация пользователя

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)  # Регистрация пользователя


current_user = fastapi_users.current_user()


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000)
