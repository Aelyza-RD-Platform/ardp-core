# Image Docker Base : Python FastAPI Service

Image Docker de base pour tous les services FastAPI Python utilisant l'infrastructure ARDP.

## 📦 Contenu

- **Python 3.11** (slim)
- **Poetry** pour gestion des dépendances
- **Dépendances FastAPI communes** :
  - `fastapi==0.104.1`
  - `uvicorn[standard]==0.24.0`
  - `pydantic==2.5.0`
  - `sqlalchemy[asyncio]==2.0.23`
  - `asyncpg==0.29.0` (PostgreSQL)
  - `redis[hiredis]==5.0.1` (Redis)
  - `python-jose[cryptography]` (JWT)
  - `passlib[bcrypt]` (Password hashing)

## 🚀 Utilisation

### Dans un Dockerfile de projet

```dockerfile
FROM 886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-python-fastapi:3.11-latest

WORKDIR /app

# Copier et installer les dépendances
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev

# Copier le code source
COPY src/ ./src/

# Commande
CMD ["uvicorn", "my_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build Local

```bash
docker build -t ardp-python-fastapi:3.11-latest -f docker-base-images/python-fastapi/Dockerfile .
```

## 📋 Tags Disponibles

- `3.11-latest` : Version Python 3.11 (latest)

## 🔗 Liens

- **ECR Repository** : `ardp-python-fastapi`
- **AWS Account** : 886220647138
- **Region** : eu-central-1

---

**Aelyza Technology** - Frankfurt am Main, Germany
