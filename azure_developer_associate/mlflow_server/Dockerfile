FROM ghcr.io/mlflow/mlflow:v3.4.0
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \ 
    && pip install azure-identity \
    && pip install azure-storage-blob 
    
EXPOSE 5000
ARG POSTGRESQL_DB_ADMIN_USERNAME
ARG POSTGRESQL_DB_ADMIN_PASSWORD
ARG POSTGRESQL_DB_NAME
ARG POSTGRESQL_SERVER


ENV POSTGRESQL_DB_ADMIN_USERNAME=${POSTGRESQL_DB_ADMIN_USERNAME}
ENV POSTGRESQL_DB_ADMIN_PASSWORD=${POSTGRESQL_DB_ADMIN_PASSWORD}
ENV POSTGRESQL_DB_NAME=${POSTGRESQL_DB_NAME}
ENV POSTGRESQL_SERVER=${POSTGRESQL_SERVER}
ENV BACKEND_STORE_URI=postgresql://${POSTGRESQL_DB_ADMIN_USERNAME}:${POSTGRESQL_DB_ADMIN_PASSWORD}@${POSTGRESQL_SERVER}:5432/${POSTGRESQL_DB_NAME}
RUN echo "My BACKEND_STORE_URI is $BACKEND_STORE_URI"
RUN echo "My POSTGRESQL_SERVER is $POSTGRESQL_SERVER"

CMD mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri "$BACKEND_STORE_URI" --default-artifact-root wasbs://mlflow-artifacts@mlflowserverstrggs.blob.core.windows.net/mlflow-artifacts
# CMD mlflow server --host 0.0.0.0 --port 5000 --default-artifact-root wasbs://mlflow-artifacts@mlflowserverstrggs.blob.core.windows.net/mlflow-artifacts
