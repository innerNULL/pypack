# file: pylocatable.sh


set -x


CONF_PATH=$1

CURR_PATH=$(pwd)
WORK_DIR="./_pylocatable"
WORK_ABS_DIR=$(cd "$(dirname "${WORK_DIR}")"; pwd)/$(basename "${WORK_DIR}")


function get_pylocatable() {
    mkdir -p ${WORK_DIR}
    cd ${WORK_DIR} && git clone git@github.com:innerNULL/pylocatable.git
}

function main() {
    get_pylocatable
    cd ${CURR_PATH}
    python3 ${WORK_DIR}/pylocatable/pack.py --conf_path ${CONF_PATH}
    rm -rf ${WORK_DIR}
}


main


