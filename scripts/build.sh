# file: build.sh


set -x


#PYTHON_BIN=$1
#MINICONDA_URL=$2
PY_ENV=$1
PY_VERSION=$2


function install_python() {
  tar -xvf *.tgz
  cd Python*
  ./configure --enable-optimizations
  make altinstall
}


function install_miniconda() {
  cd  /workspace 
  bash ./miniconda_installer.sh
  export PATH=/root/miniconda3/bin/:$PATH
  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/ 
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  conda config --add channels defaults
  conda install -c conda-forge conda-pack
  
  #conda install --file ./requirements.txt
  conda create -n ${PY_ENV} --file ./requirements.txt python=${PY_VERSION}
  conda init bash
  conda activate ${PY_ENV}
  #python -m pip install -r ./requirements.txt
  rm -rf ./${PY_ENV}.tar.gz
  conda pack -n ${PY_ENV} -o ./${PY_ENV}.tar.gz
}


function main_bak() {
  install_python
  ${PYTHON_BIN} --version
  #cd /workspace && rm -rf ./venv && mkdir ./venv && ${PYTHON_BIN} -m venv ./venv/ --copies
  ls -lh /workspace
  #ls /workspace/venv
  ${PYTHON_BIN} -m pip --upgrade pip setuptools wheel -i https://pypi.doubanio.com/simple
  ${PYTHON_BIN} -m pip uninstall conda
  ${PYTHON_BIN} -m pip install conda -i https://pypi.doubanio.com/simple
  ${PYTHON_BIN} -m pip install cytoolz -i https://pypi.doubanio.com/simple
  ${PYTHON_BIN} -m conda --version
  ${PYTHON_BIN} -m conda config --add channels https://pypi.doubanio.com/simple
  ${PYTHON_BIN} -m conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/ 
  ${PYTHON_BIN} -m conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/ 
  ${PYTHON_BIN} -m conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  ${PYTHON_BIN} -m conda config --add channels defaults
  #${PYTHON_BIN} -m conda update conda
  #cd /workspace && ${PYTHON_BIN} -m conda install --file ./requirements.txt
  cd /workspace && ${PYTHON_BIN} -m pip install -r ./requirements.txt -i https://pypi.doubanio.com/simple
  cd /workspace
  ${PYTHON_BIN} -m conda create -y -n tmp 
  ${PYTHON_BIN} -m conda activate tmp 
  ${PYTHON_BIN} -m conda pack -o ./environment.tar.gz
}


function main() {
  install_miniconda
}

main
