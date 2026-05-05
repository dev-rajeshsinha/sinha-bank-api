from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


# Define a Settings class that inherits from BaseSettings to manage application configuration
class Settings(BaseSettings):
    project_title: str
    project_version: str
    project_url: str
    application_name: str
    license_name: str
    license_url: str
    contact_name: str
    contact_email: str
    docs_url: str
    redoc_url: str
    openapi_url: str

    # Configure the Settings class to read from a .env file with UTF-8 encoding
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent.parent / ".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
    )


# Create an instance of the Settings class to load the configuration from the .env file
settings = Settings()  # pyright: ignore[reportCallIssue]
