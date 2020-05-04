FROM python:3.7

EXPOSE 5000

ARG MLFLOW_VERSION
RUN pip install mlflow==$MLFLOW_VERSION psycopg2==2.8.* && \
    mkdir -p /server

COPY ./scripts/wait-for-it.sh /server/
RUN chmod +x /server/wait-for-it.sh

WORKDIR /server

# wait as long as 60 seconds for posgres to init db, which takes a lot of time particularly in mac osx
CMD ./wait-for-it.sh ${MLFLOW_BACKEND_STORE}:${POSTGRES_PORT} -t ${WAIT_FOR_IT_TIMEOUT} -- \
    mlflow server \
    --backend-store-uri postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${MLFLOW_BACKEND_STORE}:${POSTGRES_PORT}/${POSTGRES_DATABASE} \
    --default-artifact-root /${MLFLOW_ARTIFACT_STORE} \
    --host ${MLFLOW_TRACKING_SERVER_HOST} \
    --port ${MLFLOW_TRACKING_SERVER_PORT}
