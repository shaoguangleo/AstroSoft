#!/usr/bin/env python

# This file will download sigproc and install it
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
sigproc_name= 'sigproc.tar.gz'
sigproc_size = 9999999# here to check if the file completely
#sigproc_url = 'http://www.imcce.fr/inpop/sigproc/'+sigproc_name
sigproc_git = 'https://github.com/SixByNine/sigproc.git'
configure_option = ' --prefix='+global_setting.AstroSoft_sigproc

def get_sigproc():
    #get_package.get_package(sigproc_url,sigproc_name,sigproc_size)
    os.chdir(global_setting.AstroSoft_Src)
    #print os.getcwd()
    os.system('git clone '+sigproc_git)

def install_sigproc():
    # Here will install the sigproc
    os.chdir(global_setting.AstroSoft_Src)
    os.system('tar zxvf '+ sigproc_name)
    os.chdir('sigproc')
    os.system('./bootstrap')
    #install_package.install_package(global_setting.AstroSoft_sigproc,sigproc_name,configure_option,4)
    os.system('./configure '+configure_option)
    os.system('make')
    os.system('make install')
def setting_sigproc():
    # Here will setting the sigproc
    pass

if __name__ == '__main__':
    #get_sigproc()
    install_sigproc()
