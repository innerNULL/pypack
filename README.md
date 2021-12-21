# pypack
makes PYthon environment PACKageable.  
  
By running `pypack.py` or `pypack.sh`, you can get a locatable to anywhere python environment tar.gz file. You can control which kind python environment you want by customize your config file.  
    
BTW, don't worry this will mess your current directory up, since all files and all operations will be handled or executed under `build.path` defined by config file.


## Using Scenarios
* Needs a customized python runtime for pyspark job on yarn cluster.
* Needs a specific python runtime on a server without a `sudo` account.
* Builds an unified python runtime both for offline/online/ environment, one-time's packaging, multi-scenarios' using.
* Builds a pre-built python runtime to avoid packaging process when launching a python program.


## How to Run?
Using demo config file and requirements.txt file located at `./files` as example, run
```bash
python pypack.py --conf_path ./files/centos_config.json
# or
python pypack.py --conf_path ./files/ubuntu_config.json
```
After execution, the last line of logs will tell you where to get your python-env tar.gz file.

If you do not want `git clone` the responsitory, you can just run 
```bash
curl -s https://raw.githubusercontent.com/innerNULL/pypack/main/pypack.sh | bash /dev/stdin path/to/config.json
# or (in China Mainland)
curl -s https://ghproxy.com/https://raw.githubusercontent.com/innerNULL/pypack/main/pypack.sh | bash /dev/stdin path/to/config.json
```


## Config File
* **miniconda_url**: miniconda url used to download miniconda installer.
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


## Tips
* Make sure your computer/server has enough resource (such as disk-space), since if not, conda/pip will raise hard-understanding error info.
