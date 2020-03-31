FROM python:3.7-slim

COPY docker/python-dev/requirements.txt /install/
RUN pip install -r /install/requirements.txt && \
    rm -rf /install

COPY ./ /repo/
WORKDIR /repo/
CMD ["tox"]