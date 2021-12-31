# file: pypack.sh
# date: 2021-08-23 


set -x


CONF_PATH=$1

_CURR_PATH=$(pwd)
_WORK_DIR="./_pypack"


function get_pypack() {
  mkdir -p ${_WORK_DIR}
  cd ${_WORK_DIR} && git clone git@github.com:innerNULL/pypack.git
}

function main() {
  get_pypack
  cd ${_CURR_PATH}
  python3 ${_WORK_DIR}/pypack/pypack.py --conf_path ${CONF_PATH}
  rm -rf ${_WORK_DIR}
}


main


