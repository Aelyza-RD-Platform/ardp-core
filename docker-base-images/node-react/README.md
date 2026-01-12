# Image Docker Base : Node.js React Frontend

Image Docker de base pour tous les frontends React utilisant l'infrastructure ARDP.

## 📦 Contenu

- **Node.js 20** (slim)
- **npm** (dernière version)
- **Git** pour cloner les dépendances
- **Outils système** de base

## 🚀 Utilisation

### Dans un Dockerfile de projet (Multi-stage)

```dockerfile
# Stage 1: Build
FROM 886220647138.dkr.ecr.eu-central-1.amazonaws.com/ardp-node-react:20-latest AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

# Stage 2: Production (nginx)
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Build Local

```bash
docker build -t ardp-node-react:20-latest -f docker-base-images/node-react/Dockerfile .
```

## 📋 Tags Disponibles

- `20-latest` : Version Node.js 20 (latest)

## 🔗 Liens

- **ECR Repository** : `ardp-node-react`
- **AWS Account** : 886220647138
- **Region** : eu-central-1

---

**Aelyza Technology** - Frankfurt am Main, Germany
