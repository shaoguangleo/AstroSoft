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
# Email       : sgguo@shao.ac.cn
# Institution : Shanghai Astronomical Observatory

# Test on Ubuntu 10.04 with DiFX2.0.1
sudo apt-get update
sudo apt-get upgrade

## On Lucid - Ubuntu 10.04
sudo apt-get install build-essential pkg-config bison flex libfftw3* openmpi-bin\
                      automake gfortran libexpat1-dev  libopenmpi*\
                      subversion doxygen openmpi-bin automake autoconf libtool

## on Natty & Precise (12.04)
sudo apt-get install build-essential pkg-config bison flex libfftw3-dev libopenmpi-dev \
                      openmpi-bin automake gfortran libexpat1-dev subversion libtool doxygen


## on  Trusty Tahr - Ubuntu 14.04 LTS
sudo apt-get install build-essential subversion libopenmpi-dev libfftw3-dev libtool bison \
                      flex pkg-config automake libexpat1-dev gfortran openmpi-bin doxygen


# Install Intel IPP
#Here maybe you can refer <https://software.intel.com/en-us/articles/free_ipp> for a free licence.

# Install openmpi or fftw if need

# Install DiFX
# 1. First modify the setup.bash, such as DIFXROOT,PGPLOTDIR,IPPROOT,MPICXX etc...
source setup.bash
./install-difx
./install-difx --mk5daemon
./install-difx --withmonitor
./install-difx --withfb
./install-difx --withhops
./install-difx --withguiserver
