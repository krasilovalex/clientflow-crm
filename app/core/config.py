from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME : str = 'ClientFlow CRM'
    APP_ENV : str = 'dev' # dev / prod


    POSTGRES_HOST: str = 'localhost'
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = 'clientflow'
    POSTGRES_USER: str = 'clientflow'
    POSTGRES_PASSWORD: str = 'change_me'


    JWT_SECRET_KEY: str = 'wayz'
    JWT_ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


    model_config = SettingsConfigDict(
        env_file = '.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


settings = Settings()