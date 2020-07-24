FROM alpine:3.7

MAINTAINER Brandon Spendlove <brandon.spendlove@veesix-networks.co.uk>

RUN apk --no-cache add wget curl python3 python3-dev coreutils libffi-dev libc-dev openssl-dev bash \
    && apk --no-cache add --virtual build-dependencies build-base py3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
