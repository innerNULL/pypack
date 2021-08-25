# prelocatable
makes Python environment RELOCATABLE.  
By running `python pack.py`, you can get a locatable to anywhere python environment tar.gz file. You can control which kind python environment you want by customize your config file.


## Using Scenarios
* Needs a customized python environment running pyspark job on yarn cluster.
* Needs a specific python environment on a server without a `sudo` account.
* Build a unify python environment both on offline and online environment.


## How to Run?
Using demo config file and requirements.txt file located at `./files` as example, run
```
python pack.py --conf_path ./files/config.json
```
After execution, the last line of logs will tell you where to get your python-env tar.gz file.


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
* **build**:
    * **path**: The path used to build target python environment. This should be a new path.


## TODO
* Support ubuntu platform python-env.