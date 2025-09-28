from pydantic import BaseModel, Field


class LoggingConfig(BaseModel):
    level: str = Field(..., description="Logging level")
    format: str = Field(..., description="Logging format")


class BaseConfig(BaseModel):
    app_name: str = Field(..., description="The name of the application")
    app_version: str = Field(..., description="The version of the application")
    logging: LoggingConfig = Field(..., description="Logging configuration settings")
