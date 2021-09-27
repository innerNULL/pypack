# pylocatable
makes PYthon environment reLOCATABLE.  
By running `python pack.py`, you can get a locatable to anywhere python environment tar.gz file. You can control which kind python environment you want by customize your config file.


## Using Scenarios
* Needs a customized python environment running pyspark job on yarn cluster.
* Needs a specific python environment on a server without a `sudo` account.
* Build a unify python environment both on offline and online environment.


## How to Run?
Using demo config file and requirements.txt file located at `./files` as example, run
```
python pack.py --conf_path ./files/centos_config.json
# or
python pack.py --conf_path ./files/ubuntu_config.json
```
After execution, the last line of logs will tell you where to get your python-env tar.gz file.

If you do not want `git clone` the responsitory, you can just run 
```bash
curl -s https://raw.githubusercontent.com/innerNULL/pylocatable/main/pylocatable.sh | bash /dev/stdin path/to/config.json
# or (in China Mainland)
curl -s https://ghproxy.com/https://raw.githubusercontent.com/innerNULL/pylocatable/main/pylocatable.sh | bash /dev/stdin path/to/config.json
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
    * **dep**: Target python environment's dependencies packages, which is, requirement.txt path.
    * **post_running**: The command should be executed after `pip install`.
* **build**:
    * **path**: The path used to build target python environment. This should be a new path.
    * **pre_running**: The commands should be executed before docker-building stage, usually includes specific file/data movement process.


