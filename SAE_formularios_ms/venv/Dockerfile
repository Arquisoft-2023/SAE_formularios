FROM python:3.9-slim-buster

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/
WORKDIR /app

ENV MONGODB_HOST=db
ENV MONGODB_PORT=27017
ENV MONGODB_USERNAME=admin
ENV MONGODB_PASSWORD=secret
ENV MONGODB_DB=mydatabase

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]