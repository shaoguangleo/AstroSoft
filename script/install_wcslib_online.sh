#!/usr/bin/env bash
cd ~
wget ftp://ftp.atnf.csiro.au/pub/software/wcslib/wcslib.tar.bz2
tar xvf wcslib.tar.gz
cd wcslib-*
./configure
make
sudo make install
