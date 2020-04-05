############## custom jupyter image ###############
FROM jupyter/base-notebook:latest AS jupyter-custom

RUN id 

ENV HOME_DIR=/home/$NB_USER \
    WORK_DIR=$HOME_DIR/work \
    MLFLOW_ARTIFACT_STORE=/data/artifacts

RUN conda install --quiet --yes \
    'mlflow=1.7.*' \
    'psycopg2=2.8.*' \
    'conda-build' && \
    conda build purge-all && \
    fix-permissions $CONDA_DIR && \
    fix-permissions $HOME_DIR

USER root
RUN ldconfig && \
    mkdir -p $MLFLOW_ARTIFACT_STORE && \
    chown -R $NB_UID:$NB_GID /data
    
RUN ls -la /data && \
    ls -la $MLFLOW_ARTIFACT_STORE
USER $NB_UID

################# development image ###############
FROM jupyter-custom AS editable

# Install Python dependencies from requirements.txt in advance
# Useful for development since changes in code will not trigger a layer re-build
COPY ./requirements.txt $WORK_DIR/
RUN pip install --upgrade pip && \
    pip install -r $WORK_DIR/requirements.txt

# install experiment code in editable mode
COPY ./setup.py $WORK_DIR/
COPY ./src/ $WORK_DIR/src/
USER root
RUN chown -R $NB_UID:$NB_GID $WORK_DIR/src/

USER $NB_UID
WORKDIR $WORK_DIR
RUN pip install -e .

ENTRYPOINT ["start-notebook.sh"]

################## test image ###################
FROM editable AS test

RUN pip install \
    pytest \
    pytest-dependency

COPY ./tests/docker /tests/docker
USER root
RUN chown -R $NB_UID:$NB_GID /tests/
USER $NB_UID

WORKDIR /tests

ENTRYPOINT id; \
    ls -la /data/artifacts; \
    mkdir /data/artifacts/1; \
    ls -la /data/artifacts/1; \
    sleep 5; \
    pytest -vv ./docker
