# ARDP Core

**Infrastructure R&D réutilisable - Aelyza Technology**

Ce repository contient les composants réutilisables de l'infrastructure ARDP (Aelyza R&D Platform) pour tous les projets R&D d'Aelyza Technology.

## 📦 Contenu

- **Git Templates** : Templates Cookiecutters pour créer rapidement de nouveaux projets
- **Docker Base Images** : Images Docker de base pour MCP servers, FastAPI, React
- **Terraform Modules** : Modules Terraform réutilisables pour AWS (ECR, VPC, IAM, RDS)
- **CI/CD Workflows** : Workflows GitHub Actions réutilisables

## 🏗️ Structure

```
ardp-core/
├── github-templates/          # Templates Cookiecutters
│   ├── mcp-server/           # Template pour serveur MCP
│   ├── fastapi-service/      # Template pour service FastAPI
│   └── react-frontend/        # Template pour frontend React
├── docker-base-images/        # Images Docker de base
│   ├── python-mcp/           # Image Python pour serveurs MCP
│   ├── python-fastapi/       # Image Python pour services FastAPI
│   └── node-react/            # Image Node.js pour frontends React
├── terraform-modules/         # Modules Terraform
│   ├── aws-ecr/              # Module ECR
│   ├── aws-vpc/              # Module VPC
│   ├── aws-iam/              # Module IAM
│   └── aws-rds/              # Module RDS
└── .github/workflows/         # Workflows CI/CD réutilisables
    ├── build-test.yml        # Build et tests
    ├── deploy-staging.yml    # Déploiement staging
    └── deploy-production.yml # Déploiement production
```

## 🚀 Utilisation

### Créer un nouveau projet depuis template

```bash
# Installer Cookiecutter
pip install cookiecutter

# Créer un serveur MCP
cookiecutter gh:S2Alpha/ardp-core/github-templates/mcp-server

# Créer un service FastAPI
cookiecutter gh:S2Alpha/ardp-core/github-templates/fastapi-service

# Créer un frontend React
cookiecutter gh:S2Alpha/ardp-core/github-templates/react-frontend
```

### Utiliser un module Terraform

```hcl
module "ecr_repository" {
  source = "git::https://github.com/S2Alpha/ardp-core.git//terraform-modules/aws-ecr?ref=v1.0.0"
  
  repository_name = "my-project-api"
  
  tags = {
    Project   = "MyProject"
    Component = "API"
    Company   = "Aelyza Technology"
  }
}
```

### Utiliser une image Docker

```dockerfile
FROM 886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-python-mcp:3.11-latest

WORKDIR /app
COPY . .
CMD ["python", "-m", "mcp", "run", "src/my_server.py"]
```

## 📋 Projets Supportés

- **AELYZA-Beta** : Projet IA principal
- **SADev** : Starter/template
- **SaaSAgent** : Agent autonome
- **Platform-RD** : Plateforme d'orchestration
- **Futurs projets** : Tous projets R&D Aelyza Technology

## 🔗 Liens

- **ardp-infrastructure:** https://github.com/S2Alpha/ardp-infrastructure
- **ardp-standards:** https://github.com/S2Alpha/ardp-standards
- **Documentation complète:** Voir docs/plans/MASTER_PLAN_UNIFIED_v3.1.md

## 📝 License

Propriétaire - Aelyza Technology

---

**Aelyza Technology** - Frankfurt am Main, Germany  
**AWS Account:** 886220647138
