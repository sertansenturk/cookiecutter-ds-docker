FROM python:3.7

EXPOSE 5000

RUN pip install mlflow==1.7.* psycopg2==2.8.* && \
    mkdir -p /server

COPY ./scripts/ /server/
RUN chmod +x /server/wait-for-it.sh

WORKDIR /server
CMD ./wait-for-it.sh ${MLFLOW_BACKEND_STORE}:${POSTGRES_PORT} -- mlflow server \
    --backend-store-uri postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${MLFLOW_BACKEND_STORE}:${POSTGRES_PORT}/${POSTGRES_DATABASE} \
    --default-artifact-root ${MLFLOW_ARTIFACT_STORE} \
    --host ${MLFLOW_TRACKING_SERVER_HOST} \
    --port ${MLFLOW_TRACKING_SERVER_PORT}
