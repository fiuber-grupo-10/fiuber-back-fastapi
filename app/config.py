from pydantic import BaseSettings


class Settings(BaseSettings):
    port: str = '8000'
    database_url: str = ''

    class Config:
        env_file = '../.env'


settings = Settings()
