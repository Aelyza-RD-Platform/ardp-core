# Image Docker de base pour frontends React Node.js
# Utilisée par tous les projets ARDP nécessitant un frontend React

FROM node:20-slim

LABEL org.aelyza.image.type="react-frontend-base"
LABEL org.aelyza.company="Aelyza Technology"
LABEL org.aelyza.version="20-latest"
LABEL org.aelyza.managed-by="ARDP"

# Variables d'environnement
ENV NODE_ENV=production \
    NPM_CONFIG_LOGLEVEL=warn \
    NPM_CONFIG_COLOR=false

# Installer les dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Créer le répertoire de travail
WORKDIR /app

# Installer les outils globaux (optionnel)
RUN npm install -g npm@latest

# Exposer le port par défaut
EXPOSE 3000

# Commande par défaut (peut être surchargée)
CMD ["node", "--version"]
