############## custom jupyter image ###############
FROM jupyter/scipy-notebook:862de146632b AS jupyter-custom

RUN conda install --quiet --yes \
    'mlflow=1.7.*' \
    'psycopg2=2.8.*' \
    'conda-build' \
    'tqdm' \
    'jupyter_contrib_nbextensions' \
    'jupyter_nbextensions_configurator' && \
    conda build purge-all && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

USER root
RUN ldconfig && \
    jupyter nbextension enable toc2/main --sys-prefix && \
    jupyter nbextension enable collapsible_headings/main --sys-prefix && \
    mkdir /mlflow && \
    chown -R $NB_USER:$NB_GID /mlflow
USER $NB_UID

################# development image ###############
FROM jupyter-custom AS editable

# Install Python dependencies from requirements.txt in advance
# Useful for development since changes in code will not trigger a layer re-build
COPY ./requirements.txt ./home/jovyan/work/
RUN pip install --upgrade pip && \
    pip install -r ./home/jovyan/work/requirements.txt

# install experiment code in editable mode
COPY ./setup.py /home/jovyan/work/
COPY ./src/ /home/jovyan/work/src/
USER root
RUN chown -R $NB_UID:$NB_GID /home/jovyan/work/src/

USER $NB_UID
WORKDIR /home/jovyan/work
RUN pip install -e .

ENTRYPOINT ["start-notebook.sh"]

################## test image ###################
FROM jupyter-custom AS test

RUN pip install pytest

COPY ./tests/docker /tests/docker
USER root
RUN chown -R $NB_UID:$NB_GID /tests/
USER $NB_UID

WORKDIR /tests

ENTRYPOINT sleep 5; pytest ./docker

################## static image ###################
FROM jupyter-custom AS static

COPY ./src/ /home/jovyan/work/src/
COPY ./setup.py /home/jovyan/work/

WORKDIR /home/jovyan/work
RUN pip install .

ENTRYPOINT ["start-notebook.sh"]
