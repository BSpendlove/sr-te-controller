FROM alpine:3.7

MAINTAINER Brandon Spendlove <brandon.spendlove@veesix-networks.co.uk>

RUN apk --no-cache add wget curl python3 python3-dev coreutils libffi-dev libc-dev openssl-dev bash \
    && apk --no-cache add --virtual build-dependencies build-base py3-pip \
    && pip3 install ipaddr ipy requests

ADD ./entrypoint.sh /exabgp/
COPY ./requirements.txt /exabgp/requirements.txt

WORKDIR /exabgp
RUN pip3 install -r requirements.txt
COPY . /exabgp

ENTRYPOINT ["./entrypoint.sh"]
