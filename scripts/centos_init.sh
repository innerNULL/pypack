# file: centos_init.sh


set -x


function install() {
  yum -y update
  #yum remove python3
  #yum remove python
  yum install make gcc
  yum install openssl-devel libffi-devel bzip2-devel wget git gcc-c++ -y
}


function main() {
  install
}


main
