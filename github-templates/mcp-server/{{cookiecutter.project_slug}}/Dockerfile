# Utilise l'image Docker ARDP de base
FROM {{ cookiecutter.aws_account_id }}.dkr.ecr.{{ cookiecutter.aws_region }}.amazonaws.com/ardp-python-mcp:{{ cookiecutter.python_version }}-latest

LABEL org.aelyza.project="{{ cookiecutter.project_slug }}"
LABEL org.aelyza.company="{{ cookiecutter.company }}"
LABEL org.aelyza.type="mcp-server"

WORKDIR /app

# Copier les fichiers de dépendances
COPY pyproject.toml poetry.lock* ./
COPY requirements.txt* ./

# Installer les dépendances
RUN if [ -f poetry.lock ]; then \
        pip install poetry && poetry install --no-root --no-dev; \
    elif [ -f requirements.txt ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    fi

# Copier le code source
COPY src/ ./src/

# Variables d'environnement
ENV MCP_SERVER_NAME={{ cookiecutter.server_name }}
ENV PROJECT={{ cookiecutter.project_slug }}
ENV PYTHONPATH=/app

# Exposer le port (si nécessaire)
EXPOSE 8000

# Commande par défaut
CMD ["python", "-m", "mcp", "run", "src/{{ cookiecutter.server_name }}/server.py"]
