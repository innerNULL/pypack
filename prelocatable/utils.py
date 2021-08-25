# -*- coding: utf-8 -*-
# file: utils.py


import os
from typing import Dict, List, Union, Any


def wget(url: str, target_path: str) -> str:
    target_path: str = os.path.abspath(target_path)
    target_root: str = os.path.dirname(target_path)
    os.system("mkdir -p %s" % target_root)
    
    if os.path.isfile(target_path):
        print("'%s' already exists, skip downloading." % target_path)
    else:
        cmd: str = "wget --output-document %s %s" \
                % (target_path, url)
        os.system(cmd)
    return target_path

