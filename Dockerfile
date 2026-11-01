FROM python:3.13

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .env.example .
COPY app ./app

CMD ["uvicorn", "app.main:app","--host", "0.0.0.0", "--port", "8080"]