# -*- coding: utf-8 -*-
# file: ops.py


import os
import sys
CURR_PATH: str = os.path.dirname(__file__)

import _io
from . import Config
from . import utils
from . import templates


def predownload(conf: Config) -> str:
    print("Downloading: ")
    print(utils.wget(conf.miniconda_url, conf.conda_installer))


def files_relocate(conf: Config) -> None:
    cmd: str
    scripts_path: str = os.path.join(CURR_PATH, "../scripts")
    cmd = "cp %s %s" % (
            os.path.join(scripts_path, "%s_init.sh" % conf.system), 
            conf.img_init_sh)
    os.system(cmd)

    cmd = "cp %s %s" % (
            os.path.join(scripts_path, "build.sh"), conf.build_path)
    os.system(cmd)
    cmd = "cp %s %s" % (conf.py_dep, conf.build_path)
    os.system(cmd)
    cmd = conf.pre_build_cmd
    os.system(cmd)


def dockerfile_build(conf: Config) -> str:
    dockerfile_str: str = templates.DOCKERFILE_TEMP.format(
        img = conf.base_img)
    #print(dockerfile_str)
    dockerfile: _io.TextIOWrapper = open(conf.dockerfile, "w")
    dockerfile.write(dockerfile_str)
    dockerfile.close()
    return conf.dockerfile


def img_build(conf: Config) -> str:
    cmd: str = "cd %s && docker build -t %s ./" % (
        conf.build_path, conf.build_img)
    if os.popen("docker images | grep %s" % conf.build_img)\
            .read() != "":
        print("Image %s already exists, skip building." % conf.build_img)
    else:
        os.system(cmd)
    return conf.build_img


def py_env_build(conf: Config) -> str:
    cmd: str = templates.DOCKER_RUN_TEMP.format(
        container_name=conf.container, 
        mounting_path=conf.build_path, 
        image=conf.build_img, 
        cmd="cd /workspace && bash init.sh && bash build.sh %s %s %s" \
                % (conf.py_env, str(conf.py_version), conf.post_build_cmd)
    )
    docker_img_rm_cmd: str = "sudo docker rm -f %s" % conf.container
    
    if conf.use_sudo != "1":
        cmd = cmd.replace("sudo ", "")
        docker_img_rm_cmd = docker_img_rm_cmd.replace("sudo ", "")
    
    os.system(docker_img_rm_cmd)
    os.system(cmd)

    return os.path.join(conf.build_path, conf.py_env)

