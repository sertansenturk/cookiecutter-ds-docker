FROM python:3.7-slim

ARG UNAME=devuser
ARG UID=1000
ARG GID=1000

# install git; needed for pip if the repo has git dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

COPY docker/python-dev/requirements.txt /install/
RUN pip install -r /install/requirements.txt && \
    rm -rf /install

RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME
USER $UNAME

WORKDIR /{{ cookiecutter.repo_slug }}/
CMD ["tox"]
