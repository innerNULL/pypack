# -*- coding: utf-8 -*-
#file: __init__.py


import os
import json
import _io
from typing import Dict, List, Tuple, Union, Any

from . import utils


def path_preparation(path: str) -> str:
    path: str = os.path.abspath(path)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


class Config(object):
    def __init__(self, conf_path: str):
        self.init()

        f: _io.TextIOWrapper = open(conf_path, "r")
        self._conf: Dict = json.load(f)
        f.close()
        #print(self._conf)

        self._preprocess()

    def init(self) -> None:
        self._conf: Dict

        self.miniconda_url: str
        self.base_img: str
        self.build_img: str 
        self.container: str 
        self.py_version: str 
        self.py_env: str 
        self.py_dep: str
        
        # Generated vars
        self.system: str # System info.
        self.build_path: str # All building related files path.  
        self.conda_installer: str # Conda installer path.
        self.dockerfile: str # Generated Dockerfile path.
        self.img_init_sh: str # Image initialization shell script.
        self.pre_build_cmd: str # Commands executed pre docker-building.
        self.post_build_cmd: str # Commands executed after pip install.

    def _preprocess(self) -> None:
        self.miniconda_url = self._conf["miniconda_url"]
        self.base_img = self._conf["docker"]["base_img"]
        self.build_img = self._conf["docker"]["build_img"]
        self.container = self._conf["docker"]["container"]
        self.py_version = self._conf["python"]["version"]
        self.py_env = self._conf["python"]["env_name"]
        self.py_dep = os.path.abspath(self._conf["python"]["dep"])
      
        self.system = self.get_system(self.base_img)
        self.build_path = path_preparation(
                self._conf["build"]["path"])
        self.conda_installer = os.path.join(
                self.build_path, "miniconda_installer.sh")
        self.dockerfile = os.path.join(self.build_path, "Dockerfile")
        self.img_init_sh = os.path.join(self.build_path, "init.sh")

        self.pre_build_cmd = " && ".join(self._conf["build"]["pre_running"])
        self.post_build_cmd = '\"%s\"' % ";".join(self._conf["python"]["post_running"])

    def get_system(self, img_name: str) -> str:
        if "centos" in img_name:
            return "centos"
        elif "ubuntu" in img_name:
            return "ubuntu"
        else:
            return "null"





