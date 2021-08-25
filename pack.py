# -*- coding: utf-8 -*-
# file: pack.py


import argparse
from typing import Dict, List, Union

import prelocatable as ploc
import prelocatable.ops as ops
import prelocatable.utils as utils
import prelocatable.templates as templates


argparser = argparse.ArgumentParser()
argparser.add_argument("--conf_path", 
    default="./files/config.json", type=str, help="config path.")

args = argparser.parse_args() 


if __name__ == "__main__":
    print("Starting python-env packing process...")
    conf_path: str = args.conf_path
    
    config: ploc.Config = ploc.Config(conf_path)
    ops.predownload(config)
    ops.files_relocate(config)
    ops.dockerfile_build(config)
    ops.img_build(config)
    py_env: str = ops.py_env_build(config)

    print("\nYour python-env has been put at '%s.tar.gz'." % py_env)
