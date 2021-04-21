FROM python:3.9-alpine

WORKDIR /app

ADD ./requirements.txt /app/requriements.txt

RUN pip install -r /app/requriements.txt

COPY . /app

RUN pip install .

# fix this
COPY ./service1/api/openapi.yml /usr/local/lib/python3.9/site-packages/service1/api/openapi.yml
CMD ["service1"]