#!/usr/bin/env bash
cd ../src
tar xvf wcslib.tar.gz
cd wcslib-*
./configure
make
sudo make install
