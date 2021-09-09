# file: build.sh


set -x


#PYTHON_BIN=$1
#MINICONDA_URL=$2
PY_ENV=$1
PY_VERSION=$2
POST_RUNNING_CMD=$3


function install_python() {
  tar -xvf *.tgz
  cd Python*
  ./configure --enable-optimizations
  make altinstall
}


function install_miniconda() {
  cd  /workspace 
  #bash ./miniconda_installer.sh
  bash ./miniconda_installer.sh -b
  export PATH=/root/miniconda3/bin/:$PATH
  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/ 
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  conda config --add channels defaults
  conda install -c conda-forge conda-pack --yes
}


function build_py_env() {
  cd  /workspace
  conda create -n ${PY_ENV} python=${PY_VERSION} --yes
  conda init bash
  source activate ${PY_ENV}
  python -m pip install --upgrade pip -i https://pypi.doubanio.com/simple 
  python -m pip install -r ./requirements.txt -i https://pypi.doubanio.com/simple #-vvv
}


function post_running() {
  cd /workspace
  bash -c "${POST_RUNNING_CMD}"
}


function pack_py_env() {
  rm -rf ./${PY_ENV}.tar.gz
  conda pack -n ${PY_ENV} -o ./${PY_ENV}.tar.gz
} 


function main() {
  install_miniconda
  build_py_env
  post_running
  pack_py_env
}

main
