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


cd ~
wget ftp://ftp.atnf.csiro.au/pub/software/wcslib/wcslib.tar.bz2
tar xvf wcslib.tar.gz
cd wcslib-*
./configure
make
sudo make install
