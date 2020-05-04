############## custom jupyter image ###############
ARG JUPYTER_BASE_IMAGE
ARG JUPYTER_BASE_VERSION
FROM jupyter/${JUPYTER_BASE_IMAGE}:${JUPYTER_BASE_VERSION} AS jupyter

ARG MLFLOW_ARTIFACT_STORE
ARG MLFLOW_VERSION
ENV HOME_DIR=/home/$NB_USER
ENV WORK_DIR=$HOME_DIR/work

RUN conda install --quiet --yes \
        'mlflow='$MLFLOW_VERSION \
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
    mkdir -p $MLFLOW_ARTIFACT_STORE

USER $NB_UID

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
FROM jupyter AS test

ARG TEST_DIR=/tests

COPY ./docker/jupyter/requirements.test.txt ${TEST_DIR}/
RUN pip install -r ${TEST_DIR}/requirements.test.txt

COPY ./tests/docker ${TEST_DIR}/docker
COPY ./docker/jupyter/scripts/run_pytest.sh ${TEST_DIR}/
COPY ./docker/jupyter/scripts/wait-for-it.sh ${TEST_DIR}/
USER root
RUN chmod +x ${TEST_DIR}/wait-for-it.sh
USER $NB_UID

WORKDIR ${TEST_DIR}
