from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from datetime import timedelta
from typing import Any

from fastapi.security import OAuth2PasswordRequestForm
from app.core.config import settings
from app.core.security import create_access_token, verify_password


from app.api.deps import get_db, get_current_user, get_current_active_superuser
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, Token
from app.crud.user import get_user_by_email, create_user

router = APIRouter(
    prefix="/auth",
    tags=['auth'],
)


@router.get('/ping')
def ping():
    return {'status': 'auth_ok'}

@router.post('/register', response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):

    existing = get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "User with this email already exists"
        )


    user = create_user(db, user_in)
    return user


@router.post('/login', response_model=Token)
def login_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """READ JWT TOKEN USE USERNAME (email) and password"""

    user = get_user_by_email(db, email=form_data.username)

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrent email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    

    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive User")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': str(user.id)},
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get('/me', response_model=UserRead)
def read_users_me(
    current_user: User = Depends(get_current_user)
):
    """GET DATA CURRENT USER.
    WARNING : HAVE HEADER 'Authorization: Bearer <token>' """
    return current_user

@router.get('/admin-only', response_model=UserRead)
def read_admin_data(
    current_user: User = Depends(get_current_active_superuser)
):
    
    """THIS ENDPOINT ACCESS ONLY SUPERUSER"""
    return current_user
    