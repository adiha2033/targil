
FROM ubuntu:xenial

ARG VERSION="1.2.0"
ENV VERSION=${VERSION}

RUN apt-get clean && apt-get update
RUN apt-get install -y \
    vim \
    zip \
    unzip \
    python3
COPY zip_job.py /tmp
CMD cat /etc/lsb-release && ls /tmp/zip_job.py


