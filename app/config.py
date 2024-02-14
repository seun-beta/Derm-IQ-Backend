from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    jwt_algorithm: str
    jwt_secret: str
    jwt_access_token_exp_minutes: int

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
