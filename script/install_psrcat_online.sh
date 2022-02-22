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

source astrosoft_config.sh

cd ~
wget $PSRCAT_WEBSITE/$PSRCAT_VERSION.tar.gz
tar zxvf $PSRCAT_VERSION.tar.gz

cd psrcat_tar

csh makeit

mkdir -p $ASTROSOFT/psrcat/bin
cp psrcat $ASTROSOFT/psrcat/bin
cp psrcat.db $ASTROSOFT/psrcat

export PSRCAT_FILE=$ASTROSOFT/psrcat/psrcat.db
export PATH=$PATH:$ASTROSOFT/psrcat/bin