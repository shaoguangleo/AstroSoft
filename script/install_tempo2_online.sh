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

git clone $TEMPO2_WEBSITE tempo2_src

cd tempo2_src

./bootstrap
cp -r T2runtime $ASTROSOFT/tempo2/
export TEMPO2=$ASTROSOFT/tempo2
echo "export TEMPO2=$ASTROSOFT/tempo2" >> ~/.bashrc

./configure --prefix=$ASTROSOFT/tempo2

make  
make install

make plugins
make plugins-install 
#make temponest-install