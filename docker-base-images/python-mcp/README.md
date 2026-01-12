# Image Docker Base : Python MCP Server

Image Docker de base pour tous les serveurs MCP Python utilisant l'infrastructure ARDP.

## 📦 Contenu

- **Python 3.11** (slim)
- **Poetry** pour gestion des dépendances
- **Dépendances MCP communes** :
  - `mcp==0.9.0`
  - `fastapi==0.104.1`
  - `uvicorn[standard]==0.24.0`
  - `pydantic==2.5.0`
  - `asyncpg==0.29.0` (PostgreSQL)
  - `redis[hiredis]==5.0.1` (Redis)

## 🚀 Utilisation

### Dans un Dockerfile de projet

```dockerfile
FROM 886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-python-mcp:3.11-latest

WORKDIR /app

# Copier et installer les dépendances du projet
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev

# Copier le code source
COPY src/ ./src/

# Commande
CMD ["python", "-m", "mcp", "run", "src/my_server/server.py"]
```

### Build Local

```bash
docker build -t ardp-python-mcp:3.11-latest -f docker-base-images/python-mcp/Dockerfile .
```

### Push vers ECR

```bash
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 886220647138.dkr.ecr.eu-central-1.amazonaws.com
docker tag ardp-python-mcp:3.11-latest 886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-python-mcp:3.11-latest
docker push 886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-python-mcp:3.11-latest
```

## 📋 Tags Disponibles

- `3.11-latest` : Version Python 3.11 (latest)
- `3.11-<date>` : Version datée pour versioning

## 🔗 Liens

- **ECR Repository** : `ardp-python-mcp`
- **AWS Account** : 886220647138
- **Region** : eu-central-1

---

**Aelyza Technology** - Frankfurt am Main, Germany
