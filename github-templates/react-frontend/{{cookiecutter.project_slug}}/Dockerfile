# Utilise l'image Docker ARDP Node React
FROM {{ cookiecutter.aws_account_id }}.dkr.ecr.{{ cookiecutter.aws_region }}.amazonaws.com/ardp-node-react:{{ cookiecutter.node_version }}-latest AS base

LABEL org.aelyza.project="{{ cookiecutter.project_slug }}"
LABEL org.aelyza.company="{{ cookiecutter.company }}"
LABEL org.aelyza.type="react-frontend"

WORKDIR /app

# Copier les fichiers de dépendances
COPY package.json package-lock.json* ./

# Installer les dépendances
RUN npm ci

# Copier le code source
COPY . .

# Build
FROM base AS build
RUN npm run build

# Production
FROM nginx:alpine AS production
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
