from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    password: str



class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime



class UserInDBBase(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime


class UserInDB(UserInDBBase):
    hashed_password: str