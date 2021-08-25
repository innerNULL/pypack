# -*- coding: utf-8 -*-
# file: prelocatable.py


import json
import os
from typing import Dict, List, Tuple, Any, Union


PY_RELEASE_URL_TEMP = "https://www.python.org/ftp/python/{0}/Python-{0}.tgz"
#CONDA_PY_RELEASE_TEMP = "https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh"
MINICONDA_URL = "https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh"

DOCKER_CMD_TEMP = """
sudo docker run -it --privileged \
        --name {container_name} \
        -v {mounting_path}:/workspace \
        --net=host \
        {image} \
        bash -c '{cmd}'
"""


class Config(object):
    def __init__(self):
        self.build_path: str = "./build"
        self.miniconda_url: str = "https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh"

    def init(self):
        pass


def path_preparation(path: str) -> str:
    path: str = os.path.abspath(path)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def predownload(conf: Config) -> str:
    build_path: str = path_preparation(conf.build_path)
    miniconda_installer: str = os.path.join(build_path, "miniconda_installer.sh")
    if not os.path.isfile(miniconda_installer):
        print("downloading miniconda from %s to %s" % (conf.miniconda_url, miniconda_installer))
        cmd: str = "cd %s && wget --output-document miniconda_installer.sh %s" % (
                build_path, conf.miniconda_url)
        os.system(cmd)
    else:
        print("miniconda installer already exists at '%s'" % miniconda_installer)
    return miniconda_installer



def build_dockerfile(
    base_img: str, build_path: str="./", 
    dockerfile_temp: str="./files/Dockerfile.temp", 
    maintainer: str="prelocatable@github", 
) -> str:
    build_path: str = path_preparation(build_path) 

    dockerfile: str = open(dockerfile_temp)\
            .read()\
            .replace("{__IMAGE__}", base_img)\
            .replace("{__MAINTAINER__}", maintainer)

    build_dockerfile: str = os.path.join(build_path, "Dockerfile")
    f = open(build_dockerfile, "w")
    f.write(dockerfile)
    f.close()
    return build_dockerfile 


def get_py_release(
    version: str="3.9.5", build_path: str="./build"
) -> str:
    build_path: str = path_preparation(build_path)
    py_url: str = PY_RELEASE_URL_TEMP.format(version)
    py_release_name: str = os.path.split(py_url)[-1]
    py_tar_path: str = os.path.join(build_path, py_release_name)

    if os.path.isfile(py_tar_path):
        print("file '%s' already exists!" % py_tar_path)
    else:
        cmd: str = "cd %s && wget %s" % (build_path, py_url)
        os.system(cmd)
    return py_tar_path


def build_img(img_name: str, build_path: str="./build") -> str:
    img_os: str
    if "cent" in open(os.path.join(build_path, "Dockerfile")).read():
        img_os = "centos"
        os.system("cp ./scripts/centos_init.sh %s/init.sh" % build_path)
    
    cmd: str = "cd %s && cp ../scripts/*.sh ./ && docker build -t %s ./" \
            % (build_path, img_name)
    os.system(cmd)
    return img_name


def build_py(img_name: str, build_path: str, py_bin: str) -> None:
    build_path: str = path_preparation(build_path)
    os.system("cp ./files/requirements.txt %s" % build_path)
    print("Mounting '%s'" % build_path)
    run_cmd: str = DOCKER_CMD_TEMP.format(
        container_name="prelocatable_container", 
        mounting_path=build_path, 
        image=img_name, 
        #cmd="cd /workspace && bash init.sh && bash build.sh {py_bin} {miniconda}".format(py_bin=py_bin, miniconda=MINICONDA_URL)
        cmd="cd /workspace && bash init.sh && bash build.sh"
    )
    print(run_cmd)
    os.system("sudo docker rm -f prelocatable_container")
    os.system(run_cmd)


def build_miniconda(url: str = MINICONDA_URL) -> None:
    os.system("wget %s" % url)



if __name__ == "__main__":
    conf: Config = Config()
    base_img: str = "centos:centos7.3.1611"
    build_path: str = "./build"
    py_version: str = "3.7.5"
    py_bin: str = "python" + ".".join(py_version.split(".")[:2])

    predownload(conf)
    dockerfile: str = build_dockerfile(base_img, build_path)
    #py_release: str = get_py_release(py_version, build_path)
    img: str = build_img("centos_py39", build_path)
    build_py(img, build_path, py_bin)

