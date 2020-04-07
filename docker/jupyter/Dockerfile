############## custom jupyter image ###############
FROM jupyter/scipy-notebook:862de146632b AS jupyter-custom

ARG MLFLOW_ARTIFACT_STORE

ENV HOME_DIR=/home/$NB_USER
ENV WORK_DIR=$HOME_DIR/work

RUN id  && \
    conda install --quiet --yes \
        'mlflow=1.7.*' \
        'psycopg2=2.8.*' \
        'conda-build' \
        'tqdm' \
        'jupyter_contrib_nbextensions' \
        'jupyter_nbextensions_configurator' && \
    conda build purge-all && \
    fix-permissions $CONDA_DIR && \
    fix-permissions $HOME_DIR

USER root
RUN ldconfig && \
    jupyter nbextension enable toc2/main --sys-prefix && \
    jupyter nbextension enable collapsible_headings/main --sys-prefix && \
    mkdir -p $MLFLOW_ARTIFACT_STORE && \
    chown -R $NB_UID:$NB_GID /data

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

ENTRYPOINT sleep 5; pytest -vv ./docker

################## static image ###################
FROM jupyter-custom AS static

COPY ./src/ $WORK_DIR/src/
COPY ./setup.py $WORK_DIR/

WORKDIR $WORK_DIR
RUN pip install .
