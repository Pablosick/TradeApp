from typing import Optional

from fastapi_users import schemas


# Схемы предназначены для пользовательских запросов
class UserRead(schemas.BaseUser[int]):
    """Схема для чтения пользователя"""
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    """Схема для создания пользователя"""
    username: str
    role_id: int
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
