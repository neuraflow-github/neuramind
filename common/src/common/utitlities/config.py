import os

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class MyConfig(BaseSettings):
    # Keep sorted
    azure_openai_api_key: str = Field(env="AZURE_OPENAI_API_KEY")
    azure_openai_endpoint: str = Field(env="AZURE_OPENAI_ENDPOINT")

    @property
    def logs_dir_path(self) -> str:
        return os.path.join(self.datastore_dir_path, "00_logs")

    @property
    def data_dir_path(self) -> str:
        return os.path.join(self.datastore_dir_path, "10_data")

    @property
    def temp_dir_path(self) -> str:
        return os.path.join(self.datastore_dir_path, "20_temp")

    class Config:
        env_file = ".env"
        extra = "allow"


config = MyConfig()
