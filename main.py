from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import router as api_v1_router

# Create FastAPI app
app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_v1_router, prefix=settings.API_V1_STR)
