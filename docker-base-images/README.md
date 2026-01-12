# Docker Base Images - ARDP

Images Docker de base réutilisables pour tous les projets ARDP.

## 📦 Images Disponibles

### 1. ardp-python-mcp:3.11-latest

**Usage:** Serveurs MCP Python

**Contenu:**
- Python 3.11 slim
- Dépendances MCP communes (mcp, fastapi, uvicorn, pydantic)
- Support PostgreSQL (asyncpg)
- Support Redis (redis)

**ECR:** `886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-python-mcp:3.11-latest`

---

### 2. ardp-python-fastapi:3.11-latest

**Usage:** Services FastAPI Python

**Contenu:**
- Python 3.11 slim
- FastAPI, Uvicorn, Pydantic
- SQLAlchemy async
- Support PostgreSQL et Redis
- JWT et password hashing

**ECR:** `886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-python-fastapi:3.11-latest`

---

### 3. ardp-node-react:20-latest

**Usage:** Frontends React Node.js

**Contenu:**
- Node.js 20 slim
- npm (dernière version)
- Git pour dépendances

**ECR:** `886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-node-react:20-latest`

---

## 🚀 Build et Push

### Automatique (GitHub Actions)

Les images sont automatiquement buildées et pushées vers ECR lors de :
- Push vers `main` avec modifications dans `docker-base-images/`
- Workflow manuel déclenché

**Workflow:** `.github/workflows/build-docker-images.yml`

### Manuel

```bash
# Login ECR
aws ecr get-login-password --region eu-central-1 | \
  docker login --username AWS --password-stdin \
  886220647138.dkr.ecr.eu-central-1.amazonaws.com

# Build et push python-mcp
docker build -t ardp-python-mcp:3.11-latest docker-base-images/python-mcp/
docker tag ardp-python-mcp:3.11-latest \
  886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-python-mcp:3.11-latest
docker push 886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-python-mcp:3.11-latest

# Build et push python-fastapi
docker build -t ardp-python-fastapi:3.11-latest docker-base-images/python-fastapi/
docker tag ardp-python-fastapi:3.11-latest \
  886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-python-fastapi:3.11-latest
docker push 886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-python-fastapi:3.11-latest

# Build et push node-react
docker build -t ardp-node-react:20-latest docker-base-images/node-react/
docker tag ardp-node-react:20-latest \
  886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-node-react:20-latest
docker push 886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-node-react:20-latest
```

## 📋 Versioning

- **latest** : Dernière version stable
- **{version}-{date}** : Version datée (ex: `3.11-20260112`)

## 🔗 Liens

- **ECR Registry** : `886220647138.dkr.ecr.eu-central-1.amazonaws.com`
- **AWS Account** : 886220647138
- **Region** : eu-central-1

---

**Aelyza Technology** - Frankfurt am Main, Germany
