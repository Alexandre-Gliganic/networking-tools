#!/bin/sh
docker stop networking-tools
docker rm networking-tools
docker build -t alexandre/bot .
docker run -it -d --restart=always --name networking-tools alexandre/bot:latest
