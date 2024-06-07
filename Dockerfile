# Development stage for installing dependencies
FROM python:3.11.5-slim-bullseye as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Create a virtual environment for dependencies
RUN python3 -m venv /venv

# Set the working directory
WORKDIR /app

# Copy only the dependency files for installation
COPY pyproject.toml poetry.lock /app/

# Install project dependencies using Poetry
RUN /venv/bin/pip install poetry
RUN /venv/bin/poetry install
RUN /venv/bin/poetry add gunicorn
RUN /venv/bin/poetry add loggly-python-handler

# Copy the entire application code
COPY . /app/

# Production stage for the final image
FROM base as production

# Set environment variables
ENV FLASK_ENV=production

# Configure for production (use Gunicorn)
ENTRYPOINT ["/venv/bin/poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000", "todo_app.app:create_app()"]

# Expose port 5000 for documentation
EXPOSE 5000

# Development stage for the final image
FROM base as development

# Set environment variables
ENV FLASK_ENV=development
ENTRYPOINT [ "/venv/bin/poetry", "run", "flask", "run", "--host", "0.0.0.0" ] move

# Testing stage
FROM base as test

# Set environment variables
ENV FLASK_ENV=test

# Run tests using pytest
ENTRYPOINT ["/venv/bin/poetry", "run", "pytest"]

FROM test as securityscan
ENTRYPOINT ["/venv/bin/poetry", "run", "safety", "check"]