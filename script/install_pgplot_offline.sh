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
sudo mkdir -p /usr/local/pgplot
sudo cp -rvf build/* /usr/local/pgplot
echo "Now Finished install PGPLOT5.2..."
echo "Setting the PGPLOT environment"
echo "export PGPLOT_DIR=/usr/local/pgplot" >> ~/.bashrc
echo "export PGPLOT_DEV=/Xserve" >> ~/.bashrc
echo "Enjoy."
