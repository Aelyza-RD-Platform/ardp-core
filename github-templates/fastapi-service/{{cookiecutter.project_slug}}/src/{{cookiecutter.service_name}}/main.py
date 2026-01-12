"""
FastAPI Service principal pour {{ cookiecutter.project_name }}
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

# Configuration
SERVICE_NAME = "{{ cookiecutter.service_name }}"
SERVICE_VERSION = "0.1.0"

# Créer l'application FastAPI
app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.description }}",
    version=SERVICE_VERSION,
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À configurer selon vos besoins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

{% if cookiecutter.use_postgres == "y" %}
# Configuration PostgreSQL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/dbname")

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    """Dependency pour obtenir une session DB"""
    async with AsyncSessionLocal() as session:
        yield session
{% endif %}

{% if cookiecutter.use_redis == "y" %}
# Configuration Redis
import redis.asyncio as redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
redis_client = None

@app.on_event("startup")
async def startup_event():
    """Initialisation au démarrage"""
    global redis_client
    redis_client = await redis.from_url(REDIS_URL)

@app.on_event("shutdown")
async def shutdown_event():
    """Nettoyage à l'arrêt"""
    if redis_client:
        await redis_client.close()
{% endif %}

# Modèles Pydantic
class HealthResponse(BaseModel):
    status: str
    service: str
    version: str

# Routes
@app.get("/health", response_model=HealthResponse)
async def health():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        service=SERVICE_NAME,
        version=SERVICE_VERSION
    )

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
        "status": "running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port={{ cookiecutter.port }})
