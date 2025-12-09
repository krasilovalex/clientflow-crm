from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


def get_database_url() -> str:

    if settings.APP_ENV == 'dev':

        return 'sqlite:///./clientflow.db'
    

    return (
        f"postgresql+psycopg2://{settings.POSTGRES_USER}:"
        f"{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:"
        f"{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
    )


SQLALCHEMY_DATABASE_URL = get_database_url()


if  SQLALCHEMY_DATABASE_URL.startswith('sqlite'):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False}
    )
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)