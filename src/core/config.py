from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


# Define a Settings class that inherits from BaseSettings to manage application configuration
class Settings(BaseSettings):
    # Retrieve project metadata with setting default values
    project_title: str = "Sinha Bank API"
    project_version: str = "1.0.0"
    project_url: str = "http://localhost:8000"

    # Retrieve application specific settings with setting default values
    application_name: str = "sinha_bank_api"

    # Retrieve license information with setting default values
    license_name: str = "MIT License"
    license_url: str = "https://opensource.org/licenses/MIT"

    # Retrieve contact information with setting default values
    contact_name: str = "Your Name"
    contact_email: str = "your.email@example.com"

    # Retrieve API documentation settings with setting default values
    docs_url: str = "/api/docs"
    redoc_url: str = "/api/redoc"
    openapi_url: str = "/api/openapi.json"

    # Configure the Settings class to read from a .env file with UTF-8 encoding
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent.parent / ".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
    )


# Create an instance of the Settings class to load the configuration from the .env file
settings = Settings()  # pyright: ignore[reportCallIssue]
