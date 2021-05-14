#!/bin/bash
docker network create my-net
export DOCKER_BUILDKIT=0 
docker build . -t project --network my-net
docker run -it project
