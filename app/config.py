from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str
    jwt_algorithm: str
    jwt_secret: str
    jwt_access_token_exp_minutes: int
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
