FROM python:3.7-slim

COPY ./requirements.dev.txt /code/
WORKDIR /code
RUN pip install -r requirements.dev.txt

CMD ["tox"]