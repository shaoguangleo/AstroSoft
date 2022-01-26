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

git clone $PSRCHIVE_WEBSITE psrchive_src


source $ASTROSOFT/start_tempo2.rc
source $ASTROSOFT/start_pgplot.rc
source $ASTROSOFT/start_psrcat.rc
export PSRCHIVE=$ASTROSOFT/psrchive
export PATH=$PATH:$PSRCHIVE/bin
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ASTROSOFT/epsic/lib

cd psrchive_src 
./packages/epsic.csh
./bootstrap
./configure --prefix=$ASTROSOFT/psrchive --with-cfitsio-dir=$ASTROSOFT/cfitsio --enable-shared CFLAGS=-fPIC FFLAGS=-fPIC

make  
make install
make clean