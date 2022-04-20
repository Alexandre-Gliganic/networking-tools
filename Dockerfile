# syntax=docker/dockerfile:1

FROM ubuntu:latest
RUN apt update
RUN apt upgrade -y
RUN TZ=Etc/UTC apt install tzdata -y
RUN apt install python3-pip git wget curl software-properties-common ca-certificates -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install python3.10 -y
RUN apt install python3.10-distutils -y
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

RUN apt install iputils-ping traceroute dnsutils host whois -y


WORKDIR /app

COPY requierements.txt requirements.txt
RUN python3.10 -m pip install -r requirements.txt
COPY . .

CMD ["python3.10", "network.py" ]
