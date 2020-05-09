FROM python:3.7-slim

RUN useradd -ms /bin/bash cookiecutteruser && \
    mkdir /project && \
    chown -R cookiecutteruser /project && \
    pip install cookiecutter

USER cookiecutteruser
WORKDIR /project

ENTRYPOINT cookiecutter ./ --output-dir /project/tmp/ $CUT_OPTS