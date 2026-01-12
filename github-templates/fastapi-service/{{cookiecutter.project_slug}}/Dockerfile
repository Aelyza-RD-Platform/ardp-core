# Utilise l'image Docker ARDP FastAPI
FROM {{ cookiecutter.aws_account_id }}.dkr.ecr.{{ cookiecutter.aws_region }}.amazonaws.com/ardp-python-fastapi:{{ cookiecutter.python_version }}-latest

LABEL org.aelyza.project="{{ cookiecutter.project_slug }}"
LABEL org.aelyza.company="{{ cookiecutter.company }}"
LABEL org.aelyza.type="fastapi-service"

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
ENV SERVICE_NAME={{ cookiecutter.service_name }}
ENV PROJECT={{ cookiecutter.project_slug }}
ENV PYTHONPATH=/app
ENV PORT={{ cookiecutter.port }}

# Exposer le port
EXPOSE {{ cookiecutter.port }}

# Commande par défaut
CMD ["uvicorn", "{{ cookiecutter.service_name }}.main:app", "--host", "0.0.0.0", "--port", "{{ cookiecutter.port }}"]
