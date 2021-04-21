FROM python:3.9-alpine

WORKDIR /app

ADD requirements.txt /app/requriements.txt

RUN pip install -r /app/requriements.txt

COPY . /app

RUN pip install .

# fix this
COPY ./receiver_service/api/openapi.yml /usr/local/lib/python3.9/site-packages/receiver_service/api/openapi.yml
CMD ["receiver_service"]