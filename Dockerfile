# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.7

# Allow docker to cache installed dependencies
WORKDIR /app

# Mount the application code to the image
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["gunicorn", "--bind", ":8000", "financetrust_dev_test.wsgi:application"]