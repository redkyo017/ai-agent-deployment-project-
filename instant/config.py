from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: str

    # Pydantic will load from a .env file for local development
    # while relying on system environment variables in production.
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings = Settings()