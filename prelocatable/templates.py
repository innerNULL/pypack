# -*- coding: utf-8 -*-
# file: templates.py


DOCKERFILE_TEMP: str = """
FROM {img} 
MAINTAINER "prelocatable@github"

RUN mkdir /workspace
WORKDIR /workspace

COPY ./init.sh /workspace
#COPY ./build.sh /workspace

RUN bash ./init.sh
#RUN bash ./build.sh
"""


DOCKER_RUN_TEMP = """
sudo docker run -it --privileged \
        --name {container_name} \
        -v {mounting_path}:/workspace \
        --net=host \
        {image} \
        bash -c '{cmd}'
"""
