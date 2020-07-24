FROM alpine:3.7

MAINTAINER Brandon Spendlove <brandon.spendlove@veesix-networks.co.uk>

EXPOSE 179

RUN apk --no-cache add wget curl python3 python3-dev coreutils libffi-dev libc-dev openssl-dev bash \
    && apk --no-cache add --virtual build-dependencies build-base py3-pip \
    && pip3 install ipaddr exabgp ipy requests

ADD entrypoint.sh /
COPY ./requirements.txt /exabgp/requirements.txt

WORKDIR /exabgp
RUN pip3 install -r requirements.txt
COPY . /exabgp

ENTRYPOINT ["/entrypoint.sh"]
CMD ["exabgp"]
