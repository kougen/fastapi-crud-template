FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

LABEL maintainer="Joshua Hegedus <josh.hegedus@outlook.com>"
LABEL version="1.0"
LABEL description="A simple Python web application using FastAPI. Change the labels to your own repository."
LABEL vendor="Joshua Hegedus"
LABEL license="MIT"
LABEL url="https://kou-gen.net/projects/fastapi-crud-template"
LABEL schema-version="1.0"

# NOTE: Change the following labels to your own repository. This will link the image to your repository.
LABEL org.opencontainers.image.source="https://github.com/kougen/fastapi-crud-template"
LABEL org.opencontainers.image.title="FastAPI CRUD Template"
LABEL org.opencontainers.image.description="A simple Python web application using FastAPI. Change the labels to your own repository."
LABEL org.opencontainers.image.url="https://kou-gen.net/projects/fastapi-crud-template"
LABEL org.opencontainers.image.documentation="https://kou-gen.net/projects/fastapi-crud-template"
