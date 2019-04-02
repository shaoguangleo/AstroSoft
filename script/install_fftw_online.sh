#!/usr/bin/env bash
#
#     _        _            ____         __ _
#    / \   ___| |_ _ __ ___/ ___|  ___  / _| |_
#   / _ \ / __| __| '__/ _ \___ \ / _ \| |_| __|
#  / ___ \\__ \ |_| | | (_) |__) | (_) |  _| |_
# /_/   \_\___/\__|_|  \___/____/ \___/|_|  \__|
#
#
# Author      : Guo Shaoguang
# Email       : shaoguangleo@gmail.com
# Institution : Shanghai Astronomical Observatory

source astrosoft_config.sh

cd ~
wget http://www.fftw.org/fftw-3.3.8.tar.gz
tar zxvf fftw-3.3.8.tar.gz
cd fftw-3.3.8

# for psrchive
$ ./configure --prefix=$ASTROSOFT --enable-float --enable-threads --enable-shared CFLAGS=-fPIC FFLAGS=-fPIC
make
make check
make install
make clean
# for tempo2
./configure --prefix=$ASTROSOFT CFLAGS=-fPIC FFLAGS=-fPIC
make
make check
make install
make clean
