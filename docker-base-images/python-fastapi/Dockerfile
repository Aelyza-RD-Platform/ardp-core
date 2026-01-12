# Image Docker de base pour services FastAPI Python
# Utilisée par tous les projets ARDP nécessitant un service FastAPI

FROM python:3.11-slim

LABEL org.aelyza.image.type="fastapi-service-base"
LABEL org.aelyza.company="Aelyza Technology"
LABEL org.aelyza.version="3.11-latest"
LABEL org.aelyza.managed-by="ARDP"

# Variables d'environnement
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Installer les dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Installer Poetry
RUN pip install --no-cache-dir poetry==1.7.1 && \
    poetry config virtualenvs.create false

# Dépendances FastAPI communes
RUN pip install --no-cache-dir \
    fastapi==0.104.1 \
    uvicorn[standard]==0.24.0 \
    pydantic==2.5.0 \
    pydantic-settings==2.1.0 \
    python-multipart==0.0.6 \
    python-jose[cryptography]==3.3.0 \
    passlib[bcrypt]==1.7.4 \
    sqlalchemy[asyncio]==2.0.23 \
    asyncpg==0.29.0 \
    redis[hiredis]==5.0.1 \
    httpx==0.25.2 \
    python-dotenv==1.0.0

# Créer le répertoire de travail
WORKDIR /app

# Exposer le port par défaut
EXPOSE 8000

# Commande par défaut (peut être surchargée)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
