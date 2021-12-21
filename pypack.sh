# file: pypack.sh


set -x


CONF_PATH=$1

CURR_PATH=$(pwd)
WORK_DIR="./_pypack"
WORK_ABS_DIR=$(cd "$(dirname "${WORK_DIR}")"; pwd)/$(basename "${WORK_DIR}")


function get_pypack() {
    mkdir -p ${WORK_DIR}
    cd ${WORK_DIR} && git clone git@github.com:innerNULL/pypack.git
}

function main() {
    get_pypack
    cd ${CURR_PATH}
    python3 ${WORK_DIR}/pypack/pypack.py --conf_path ${CONF_PATH}
    rm -rf ${WORK_DIR}
}


main


