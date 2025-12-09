from typing import Generator, Optional


from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.user import User
from app.db.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


o2auth_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(
        token: str = Depends(o2auth_scheme),
        db: Session = Depends(get_db)
) -> User:
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:

        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )

        user_id_str : str = payload.get('sub')

        if user_id_str is None:
            raise credentials_exception
        
        user_id = int(user_id_str)
    
    except (JWTError, ValueError):
        raise credentials_exception
    

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise credentials_exception


    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Inactive user'
        )
    
    return user


def get_current_active_superuser(
        current_user: User = Depends(get_current_user),
) -> User:
    """CHECK SUPERUSERACTIVE if no 403"""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough priviliges"
        )
    return current_user