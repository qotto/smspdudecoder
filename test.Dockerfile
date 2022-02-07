FROM ubuntu:latest

RUN apt update
RUN apt install -y software-properties-common curl

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt install -y \
    python3.7 python3.7-distutils \
    python3.8 python3.8-distutils \
    python3.9 python3.9-distutils \
    python3.10 python3.10-distutils

RUN curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.7 get-pip.py
RUN python3.8 get-pip.py
RUN python3.9 get-pip.py
RUN python3.10 get-pip.py
RUN rm get-pip.py

RUN python3.10 -m pip install tox

WORKDIR /src
ADD . /src
