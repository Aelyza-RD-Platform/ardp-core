# Image Docker de base pour serveurs MCP Python
# Utilisée par tous les projets ARDP nécessitant un serveur MCP

FROM python:3.11-slim

LABEL org.aelyza.image.type="mcp-server-base"
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

# Installer Poetry pour la gestion des dépendances
RUN pip install --no-cache-dir poetry==1.7.1 && \
    poetry config virtualenvs.create false

# Dépendances MCP communes pour tous les serveurs
# Note: Utiliser fastapi>=0.115.0 pour compatibilité avec mcp et anyio>=4.6
RUN pip install --no-cache-dir \
    mcp==0.9.1 \
    fastapi==0.115.0 \
    uvicorn[standard]==0.32.0 \
    pydantic==2.9.0 \
    pydantic-settings==2.5.0 \
    anyio>=4.6.0 \
    asyncpg==0.29.0 \
    redis[hiredis]==5.0.1 \
    httpx==0.27.0 \
    python-dotenv==1.0.0

# Créer le répertoire de travail
WORKDIR /app

# Exposer le port par défaut
EXPOSE 8000

# Commande par défaut (peut être surchargée)
CMD ["python", "-m", "mcp"]
