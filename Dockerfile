FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]