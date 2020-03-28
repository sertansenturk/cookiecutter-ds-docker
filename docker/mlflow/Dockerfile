FROM python:3.7

EXPOSE 5000

RUN pip install mlflow==1.7.* psycopg2==2.8.* && \
    mkdir -p /server

COPY ./scripts/ /server/
RUN chmod +x /server/wait-for-it.sh

WORKDIR /server
CMD ./wait-for-it.sh postgres:5432 -- mlflow server \
    --backend-store-uri postgresql://admin:secret@postgres:5432/mlflow \
    --default-artifact-root /mlflow \
    --host 0.0.0.0 \
    --port 5000
