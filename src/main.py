from fastapi import FastAPI
from src.core.config import settings

# Initialize the FastAPI application
sinha_bank_api = FastAPI(
    title=settings.project_title,
    version=settings.project_version,
    contact={
        "name": settings.contact_name,
        "email": settings.contact_email,
        "url": settings.project_url,
    },
    license_info={
        "name": settings.license_name,
        "url": settings.license_url,
    },
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url,
    openapi_url=settings.openapi_url,
)


# Define a simple health check endpoint
@sinha_bank_api.get("/api/health")
async def health_check():
    return {
        "application_name": settings.application_name,
        "version": settings.project_version,
        "status": "operational",
    }
