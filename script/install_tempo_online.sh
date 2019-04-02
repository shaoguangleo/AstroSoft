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

git clone $TEMPO_WEBSITE tempo_src

cd tempo_src

./prepare  
./configure --prefix=$ASTROSOFT/tempo
make  
make install
cp -rv clock ephem tzpar util $ASTROSOFT/tempo
cp tempo.hlp $ASTROSOFT/tempo
cp obsys.dat $ASTROSOFT/tempo
echo "export PATH=$PATH:$ASTROSOFT/tempo/bin" >> ~/.bashrc
echo "export TEMPO=$ASTROSOFT/tempo" >> ~/.bashrc
echo "export CLKDIR=$ASTROSOFT/tempo/clock" >> ~/.bashrc
echo "export PARDIR=$ASTROSOFT/tempo/tzpar" >> ~/.bashrc
echo "export EPHDIR=$ASTROSOFT/tempo/ephem" >> ~/.bashrc
echo "export OBSYS=$ASTROSOFT/tempo/obsys.dat" >> ~/.bashrc