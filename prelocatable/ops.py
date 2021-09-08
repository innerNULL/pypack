# -*- coding: utf-8 -*-
# file: ops.py


import os
import _io
from . import Config
from . import utils
from . import templates


def predownload(conf: Config) -> str:
    print("Downloading: ")
    print(utils.wget(conf.miniconda_url, conf.conda_installer))


def files_relocate(conf: Config) -> None:
    cmd: str
    cmd = "cp %s %s" % (
        "./scripts/%s_init.sh" % conf.system, conf.img_init_sh)
    os.system(cmd)

    cmd = "cp %s %s" % ("./scripts/build.sh", conf.build_path)
    os.system(cmd)
    cmd = "cp %s %s" % (conf.py_dep, conf.build_path)
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
    os.system("sudo docker rm -f %s" % conf.container)
    os.system(cmd)
    os.system("sudo chmod 777 %s.tar.gz" 
            % os.path.join(conf.build_path, conf.py_env))
    return os.path.join(conf.build_path, conf.py_env)

