from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class MyConfig(BaseSettings):
    # Keep sorted
    port: int = Field(env="PORT", default=8000)
    testbench_connectors_path: str = Field(env="TESTBENCH_CONNECTORS_PATH")

    class Config:
        env_file = ".env"
        extra = "allow"


config = MyConfig()
