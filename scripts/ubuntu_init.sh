# file: ubuntu_init.sh


set -x


function install() {
  echo "deb http://mirrors.aliyun.com/ubuntu/ vivid main restricted universe multiverse" >> /etc/apt/sources.list
  echo "deb http://mirrors.aliyun.com/ubuntu/ vivid-security main restricted universe multiverse" >> /etc/apt/sources.list
  echo "deb http://mirrors.aliyun.com/ubuntu/ vivid-updates main restricted universe multiverse" >> /etc/apt/sources.list
  echo "deb http://mirrors.aliyun.com/ubuntu/ vivid-proposed main restricted universe multiverse" >> /etc/apt/sources.list
  echo "deb http://mirrors.aliyun.com/ubuntu/ vivid-backports main restricted universe multiverse" >> /etc/apt/sources.list
  echo "deb-src http://mirrors.aliyun.com/ubuntu/ vivid main restricted universe multiverse" >> /etc/apt/sources.list
  echo "deb-src http://mirrors.aliyun.com/ubuntu/ vivid-security main restricted universe multiverse" >> /etc/apt/sources.list
  echo "deb-src http://mirrors.aliyun.com/ubuntu/ vivid-updates main restricted universe multiverse" >> /etc/apt/sources.list
  echo "deb-src http://mirrors.aliyun.com/ubuntu/ vivid-proposed main restricted universe multiverse" >> /etc/apt/sources.list
  echo "deb-src http://mirrors.aliyun.com/ubuntu/ vivid-backports main restricted universe multiverse" >> /etc/apt/sources.list
  apt -y update
  apt -y install make gcc
  apt -y install zip wget git g++  
}


function main() {
  install
}


main
