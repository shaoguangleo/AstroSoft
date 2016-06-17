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


#    Fedora:
#    $ sudo yum install libX11-devel
#    $ sudo yum install gcc-gfortran
#    Ubuntu:
#    $ sudo apt-get install xorg-dev
#    $ sudo apt-get install gfortran
#    CentOS:
#    $ sudo yum install libX11-devel
#    $ sudo yum install gcc-gfortran
#    OpenSUSE:
#    $ sudo zypper install xorg-X11-devel
#    $ sudo zypper install gcc-fortran
#    Debian:
#    $ sudo apt-get install libX11-dev
#    $ sudo apt-get install gfortran

dest_dir=/home/DIFX/pgplot

echo "Now Begin install PGPLOT5.2..."
rm -rvf build
mkdir build
cd build
build_path=`pwd`
cd ../../src
rm -rvf pgplot
tar zxvf pgplot5.2.tar.gz
cd pgplot
src_location=`pwd`
cat drivers.list | sed "s;! PSDRIV;PSDRIV;g" > drivers.list.new
cat drivers.list.new | sed "s;! XWDRIV;XWDRIV;g" > drivers.list.new.new
cp drivers.list.new.new ${build_path}/drivers.list
# Do not work as src_location
cd ${build_path}
#../makemake .. linux g77_gcc_aout
#cd ../pgplot
#cat makefile | sed "s/=g77/=gfortran/g" > makefile.new
cp ../pgplot/*  .
make
make cpg
make clean
cd ..
mkdir -p ${dest_dir}
cp -rvf build/* ${dest_dir}
echo "Now Finished install PGPLOT5.2..."
echo "Setting the PGPLOT environment"
echo "export PGPLOT_DIR=${dest_dir}" >> ~/.bashrc
echo "export PGPLOT_DEV=/Xserve" >> ~/.bashrc
echo "Enjoy."
