FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

WORKDIR /app/tournoi_foot

RUN pip install --upgrade pip && pip install -r ../requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
