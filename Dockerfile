FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:5000", "--timeout", "120", "--workers", "4"]
