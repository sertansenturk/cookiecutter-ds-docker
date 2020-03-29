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
