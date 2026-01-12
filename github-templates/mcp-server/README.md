# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## 🏗️ Structure

```
{{ cookiecutter.project_slug }}/
├── src/{{ cookiecutter.server_name }}/
│   ├── __init__.py
│   ├── server.py              # Serveur MCP principal
│   └── tools/                 # Outils MCP
├── tests/
│   ├── __init__.py
│   └── test_server.py
├── Dockerfile                 # Utilise image ARDP
├── pyproject.toml            # Dépendances Python
├── terraform/                 # Infrastructure (modules ARDP)
│   └── main.tf
├── .github/workflows/         # CI/CD (hérité ARDP)
│   └── build-test.yml
└── README.md
```

## 🚀 Quick Start

### Installation

```bash
# Installer les dépendances
pip install -r requirements.txt

# Ou avec Poetry
poetry install
```

### Développement Local

```bash
# Lancer le serveur MCP
python -m mcp run src/{{ cookiecutter.server_name }}/server.py
```

### Build Docker

```bash
# Build avec image ARDP
docker build -t {{ cookiecutter.project_slug }}:latest .

# Run
docker run -p 8000:8000 {{ cookiecutter.project_slug }}:latest
```

### Déploiement

```bash
# Terraform
cd terraform
terraform init
terraform plan
terraform apply
```

## 📋 Utilise Infrastructure ARDP

- **Image Docker** : `ardp-python-mcp:3.11-latest`
- **Modules Terraform** : Depuis `ardp-core/terraform-modules`
- **Workflows CI/CD** : Hérités de `ardp-core/.github/workflows`

## 🔗 Liens

- **ARDP Core** : https://github.com/Aelyza-RD-Platform/ardp-core
- **Documentation** : Voir docs/plans/MASTER_PLAN_UNIFIED_v3.1.md

---

**Aelyza Technology** - Frankfurt am Main, Germany
