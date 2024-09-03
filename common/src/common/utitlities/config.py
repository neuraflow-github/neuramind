import os

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class MyConfig(BaseSettings):
    # Keep sorted
    azure_openai_api_key: str = Field(env="AZURE_OPENAI_API_KEY")
    azure_openai_endpoint: str = Field(env="AZURE_OPENAI_ENDPOINT")

    class Config:
        env_file = ".env"
        extra = "allow"


config = MyConfig()
