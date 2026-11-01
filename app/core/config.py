from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    ALLOWED_ORIGINS: str
    POSTGRES_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env.example")
    """
    
    '.env.example' for fast test
    create your own .env file and write '.env'
    
    """

settings = Settings()
