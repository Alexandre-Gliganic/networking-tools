# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app

RUN  pip3 install git+https://github.com/Rapptz/discord.py.git@master
COPY . .

CMD ["python3", "network.py" ]
