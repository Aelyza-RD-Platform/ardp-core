# Template React Frontend

Template Cookiecutters pour créer rapidement un nouveau frontend React utilisant l'infrastructure ARDP.

## 🚀 Utilisation

```bash
# Installer Cookiecutter
pip install cookiecutter

# Générer un nouveau projet
cookiecutter gh:Aelyza-RD-Platform/ardp-core/github-templates/react-frontend
```

## 📋 Variables du Template

- `project_name` : Nom du projet
- `description` : Description du frontend
- `node_version` : Version Node.js (défaut: 20)
- `use_typescript` : Utiliser TypeScript (y/n)
- `use_tailwind` : Utiliser TailwindCSS (y/n)
- `port` : Port de développement (défaut: 3000)

## 🏗️ Structure Générée

```
project-name/
├── src/
│   ├── App.jsx
│   └── main.jsx
├── public/
├── package.json
├── vite.config.js
├── Dockerfile              # Utilise image ARDP
├── terraform/              # Infrastructure
└── .github/workflows/      # CI/CD
```

## 🔗 Infrastructure ARDP

- **Image Docker** : `ardp-node-react:20-latest`
- **Modules Terraform** : Depuis `ardp-core/terraform-modules`
- **Workflows CI/CD** : Hérités de `ardp-core`

---

**Aelyza Technology** - Frankfurt am Main, Germany
