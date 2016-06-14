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

# Test on Ubuntu 10.04 with DiFX2.0.1
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install build-essential pkg-config \
                      bison flex libfftw3-dev libopenmpi-dev openmpi-bin\
                      automake gfortran libexpat1-dev \
                      subversion doxygen openmpi-bin automake autoconf libtool

# Install Intel IPP
