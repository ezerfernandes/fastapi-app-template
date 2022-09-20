import os
from pydantic import BaseSettings, PyObject


class Settings(BaseSettings):
    environment_name: str
    connection_string: str = ''
    port: int

    # Dependency injection
    CourseRepository: PyObject

    class Config:
        env_file_encoding = "utf-8"
   
    @property
    def is_production(self) -> bool:
        return self.environment_name in ["prod"]


def get_settings() -> Settings:
    environment_name = os.getenv("ENVIRONMENT_NAME")
    if environment_name is None:
        environment_name = "dev"
    return Settings(
        environment_name=environment_name,
        _env_file = f'.env.{environment_name}',   
    )
