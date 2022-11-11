from pydantic import BaseSettings


class AppConfig(BaseSettings):
    db_username: str
    db_password: str
    db_address: str
    db_name: str

    class Config:
        env_file = '.env'


settings = AppConfig()
