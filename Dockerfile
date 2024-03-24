FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# NOTE: Change the following labels to your own repository. This will link the image to your repository.
LABEL org.opencontainers.image.source=https://github.com/kougen/fastapi-crud-template
