"""
config.settings - Configures data store using environment variables
"""
from pydantic import BaseSettings


class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
    """
    Data store configuration
    """

    DBML_VERSION: str = "v2"
    GENERATED_PATH: str = "./tds/autogen"
    DBML_PATH: str = "./askem.dbml"
    SQL_URL: str = "rdb"
    SQL_PORT: int = 8032
    SQL_USER: str = "dev"
    SQL_PASSWORD: str = "dev"


settings = Settings()
