from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.user import UserCreate, UserRead
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