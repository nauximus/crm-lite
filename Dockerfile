FROM python:3.11-slim

WORKDIR /app

#deps
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN gunicorn --version

#ENV
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]