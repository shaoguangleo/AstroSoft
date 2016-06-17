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

## On Lucid - Ubuntu 10.04
sudo apt-get install build-essential pkg-config bison flex libfftw3* openmpi-bin\
                      automake gfortran libexpat1-dev  libopenmpi*\
                      subversion doxygen openmpi-bin automake autoconf libtool

# Install DiFX

echo "Begin install the DiFX2.4.0"
sudo mkdir /home/DIFX
sudo chmod -R 777 /home/DIFX
cd ../src
tar zxvf DiFX2.4.0_on_Ubuntu10.04.tar.gz
cp -rvf /home/DIFX/* /home/DIFX/

echo "# Here for the DiFX setting" >> ~/.bashrc
echo "source /home/DIFX/difx.bash" >> ~/.bashrc

echo "Finish install the DiFX2.4.0"
echo "Enjoy!"
