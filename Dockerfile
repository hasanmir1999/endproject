FROM python:3.12.2-slim-bookworm

WORKDIR /var/www

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src/apps/api/v1 .

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]