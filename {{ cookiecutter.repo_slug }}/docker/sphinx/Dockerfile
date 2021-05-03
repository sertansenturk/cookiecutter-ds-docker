########### Below is copied from the official Sphinx image ###############
# Sphinx image is built on Python 3.8, however some requirements cannot be
# installed on Python 3.8.
# For now we copy the official Sphinx Dockerfile and base it on
# python3.7:slim instead
FROM python:3.7-slim
LABEL maintainer="Sphinx Team <https://www.sphinx-doc.org/>"
# below ARGs are our own addition
ARG SPHINX_VERSION

WORKDIR /docs
RUN apt-get update \
 && apt-get install --no-install-recommends -y \
      graphviz \
      imagemagick \
      make \
 && apt-get autoremove \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --no-cache-dir -U pip
RUN python3 -m pip install --no-cache-dir Sphinx==$SPHINX_VERSION Pillow
################ Official Sphinx image ends here #########################

ENV SPHINX_OPTS=

RUN useradd -ms /bin/bash sphinxuser && \
    mkdir /{{ cookiecutter.repo_slug }} && \
    chown -R sphinxuser /{{ cookiecutter.repo_slug }} && \
    pip install sphinx_rtd_theme

# install requirements, as well as git and gcc, which may be needed for
# some requirements
COPY requirements.txt /install/
RUN apt-get update && \
    apt-get install -y --no-install-recommends git build-essential && \
    pip install --upgrade pip && \
    pip install -r /install/requirements.txt && \
    rm -rf /install && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

USER sphinxuser

WORKDIR /{{ cookiecutter.repo_slug }}/docs

CMD make html SPHINXOPTS:=$SPHINX_OPTS
