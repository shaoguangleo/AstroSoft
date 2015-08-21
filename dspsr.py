#!/usr/bin/env python

# This file will download dspsr and install it
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
dspsr_name= 'dspsr.tar.gz'
dspsr_size = 9999999# here to check if the file completely
#dspsr_url = 'http://www.imcce.fr/inpop/dspsr/'+dspsr_name
dspsr_git = 'https://github.com/SixByNine/dspsr.git'
configure_option = ' --prefix='+global_setting.AstroSoft_dspsr

def get_dspsr():
    #get_package.get_package(dspsr_url,dspsr_name,dspsr_size)
    os.chdir(global_setting.AstroSoft_Src)
    #print os.getcwd()
    os.system('git clone '+dspsr_git)

def install_dspsr():
    # Here will install the dspsr
    os.chdir(global_setting.AstroSoft_Src)
    os.system('tar zxvf '+ dspsr_name)
    os.chdir('dspsr')
    os.system('./bootstrap')
    #install_package.install_package(global_setting.AstroSoft_dspsr,dspsr_name,configure_option,4)
    os.system('./configure '+configure_option)
    os.system('make')
    os.system('make install')
def setting_dspsr():
    # Here will setting the dspsr
    pass

if __name__ == '__main__':
    #get_dspsr()
    install_dspsr()
