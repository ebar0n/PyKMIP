FROM python:3.4

MAINTAINER PyKMIP-Team

ENV PYTHONUNBUFFERED 1

COPY ./setup.py /home/app/setup.py
COPY ./kmip /home/app/kmip

RUN cd /home/app/ \
	&& python setup.py build \
	&& python setup.py install

COPY ./bin/run_server.py /home/app/run_server.py
COPY ./pykmip /etc/pykmip
