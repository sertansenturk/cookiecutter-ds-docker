FROM python:3.7-slim

COPY ./requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

CMD ["tox"]