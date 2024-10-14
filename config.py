from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    database_host: str
    database_password: str
    database_username: str
    database_name: str
    database_port: str
    algorithm: str
    access_token_expire_time: int
    secret_key:str

    class Config:
        env_file = ".env"

settings = Setting()

print(settings.database_password)
print(settings.database_username)
