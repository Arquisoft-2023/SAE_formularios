# Use an official Python runtime as a parent image
FROM python:3

COPY . /app/
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "App:app", "--host", "0.0.0.0", "--port", "80"]