from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class MyConfig(BaseSettings):
    # Keep sorted
    port: int = Field(env="PORT")

    class Config:
        env_file = ".env"
        extra = "allow"


config = MyConfig()
