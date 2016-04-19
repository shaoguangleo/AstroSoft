#!/usr/bin/env python

# This file will download calceph and install it
import os
import terminalColor
import get_cmd_path
import global_setting
import get_package
import install_package
# Changelog
# 2015-08-20

__author__ = "Guo Shaoguang<sgguo@shao.ac.cn>"
__version__ = 1.0
__date__ = "2015-08-18"

# The download url
calceph_name= 'calceph-2.2.3.tar.gz'
calceph_size = 9999999# here to check if the file completely
calceph_url = 'http://www.imcce.fr/inpop/calceph/'+calceph_name
configure_option = '--disable-shared'

def get_calceph():
    get_package.get_package(calceph_url,calceph_name,calceph_size)

def install_calceph():
    # Here will install the calceph
    install_package.install_package(global_setting.AstroSoft_calceph,calceph_name,configure_option,4)

def setting_calceph():
    # Here will setting the calceph
    pass

if __name__ == '__main__':
    #get_calceph()
    install_calceph()
