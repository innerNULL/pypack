# pypack
makes PYthon environment PACKageable.  
  
By running `pypack.py` or `pypack.sh`, you can get a locatable to anywhere python environment tar.gz file. You can control which kind python environment you want by customize your config file.  
    
BTW, don't worry this will mess your current directory up, since all files and all operations will be handled or executed under `build.path` defined by config file.


## Using Scenarios
* Needs a customized python runtime for pyspark job on yarn cluster.
* Needs a specific python runtime on a server without a `sudo` account.
* Builds an unified python runtime both for offline/online/ environment, one-time's packaging, multi-scenarios' using.
* Builds a pre-built python runtime to avoid packaging process when launching a python program.
* Avoid some weird issues/bugs when using `python -m venv`, for example, try: 
```
python3 -venv ./pyenv --copies
source ./pyenv/bin/activate   
pip install gdown
```

## Requirements
* unix-like system
* docker with sudo authority  
* python with version higher than 3.0  

## How to Run?
Using demo config file and requirements.txt file located at `./demo_conf` as example, run
```bash
python pypack.py --conf_path ./demo_conf/pypack_centos.json
# or
python pypack.py --conf_path ./demo_conf/pypack_ubuntu.json
```
After execution, the last line of logs will tell you where to get your python-env tar.gz file.

If you do not want `git clone` the responsitory, you can just run 
```bash
curl -s https://raw.githubusercontent.com/innerNULL/pypack/main/pypack.sh | bash /dev/stdin path/to/config.json
# or (in China Mainland)
wget -qO - https://ghproxy.com/https://raw.githubusercontent.com/innerNULL/pypack/main/pypack.sh | bash /dev/stdin path/to/config.json
```

## Define Project Python-Env Building Process with Makefile
Refer to `./example`, just run `make`.


## Config File
* **miniconda_url**: miniconda url used to download miniconda installer.
* **use_sudo**: If using `sudo` to run docker or some other operations on local, in model case you should set this to "0", which means not use.
* **docker**:
    * **base_img**: Base image (and its tag) used to package python-building image.
    * **build_img**: The name of the images build on `base_img` for python environment building.
    * **container**: Container's name when running `build_img`.
* **python**:
    * **version**: Target python environment version.
    * **env_name**: Target python environment name.
    * **dep**: Target python environment's dependencies packages, which is, `requirement.txt` path. Note, no matter you use `pack.py` or `pypack.sh`, this path should be an absolute path or **a relative path refer to your current path (the path you execute packaging command)**.
    * **post_running**: The command should be executed after `pip install`.
* **build**:
    * **path**: The directroy under which to execute building target python environment. This should be a new path.
    * **pre_running**: The commands should be executed before docker-building stage, usually includes specific file/data movement process.

## Pre/Post Running Mechanism
In pypack config, there is a post-running mechanism after python modules have been installed, and a pre-running mechanism before python runtime packaging process. Using
[pypack_ubuntu.json](https://github.com/innerNULL/pypack/blob/main/demo_conf/pypack_ubuntu.json) and [requirements.txt](https://github.com/innerNULL/pypack/blob/main/demo_conf/requirements.txt) as
exmaple:  
* **post_running**: Since after we packaging python-env which contains spacy, we also hope download spacy-zh-dependencies before packaging python-env to tar.gz, but this should be executed with python-cmd, so we can just add shell command lines in `post_running`.   
* **pre_running**: Similiar with `post_running`, but this is used to do some preparation before all python-packaging process, for example, here we clone the ultipledispatch into `build.path`, so in requirements.txt we can install this module from local directory.


## Tips
* Make sure your computer/server has enough resource (such as disk-space), since if not, conda/pip will raise hard-understanding error info.
