FROM python:3.7-slim

# # install git; needed for pip if the template has git dependencies
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends git && \
#     apt-get purge -y --auto-remove && \
#     rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash cookiecutteruser && \
    mkdir /project && \
    chown -R cookiecutteruser /project && \
    pip install cookiecutter

USER cookiecutteruser
WORKDIR /project

ENTRYPOINT cookiecutter ./ --output-dir /project/tmp/ $CUT_OPTS