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
wget $CFITSIO_WEBSITE/cfitsio$CFITSIO_VERSION.tar.gz
gunzip -c cfitsio${CFITSIO_VERSION}.tar.gz | tar xvf -
cd cfitsio

./configure --prefix=$ASTROSOFT

make clean
make
make shared
make install