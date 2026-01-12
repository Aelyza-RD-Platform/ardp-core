# Template FastAPI Service

Template Cookiecutters pour créer rapidement un nouveau service FastAPI utilisant l'infrastructure ARDP.

## 🚀 Utilisation

```bash
# Installer Cookiecutter
pip install cookiecutter

# Générer un nouveau projet
cookiecutter gh:Aelyza-RD-Platform/ardp-core/github-templates/fastapi-service
```

## 📋 Variables du Template

- `project_name` : Nom du projet
- `service_name` : Nom du service (généré automatiquement)
- `description` : Description du service
- `python_version` : Version Python (défaut: 3.11)
- `use_postgres` : Utiliser PostgreSQL (y/n)
- `use_redis` : Utiliser Redis (y/n)
- `port` : Port du service (défaut: 8000)

## 🏗️ Structure Générée

```
project-name/
├── src/service_name/
│   ├── __init__.py
│   └── main.py              # Application FastAPI
├── tests/
│   └── test_main.py
├── Dockerfile               # Utilise image ARDP
├── pyproject.toml          # Dépendances
├── terraform/              # Infrastructure
└── .github/workflows/      # CI/CD
```

## 🔗 Infrastructure ARDP

- **Image Docker** : `ardp-python-fastapi:3.11-latest`
- **Modules Terraform** : Depuis `ardp-core/terraform-modules`
- **Workflows CI/CD** : Hérités de `ardp-core`

---

**Aelyza Technology** - Frankfurt am Main, Germany
