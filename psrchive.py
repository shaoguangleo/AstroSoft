#!/usr/bin/env python

# This file will download psrchive and install it
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
psrchive_name= 'psrchive.tar.gz'
psrchive_size = 9999999# here to check if the file completely
#psrchive_url = 'http://www.imcce.fr/inpop/psrchive/'+psrchive_name
psrchive_git = 'https://github.com/SixByNine/psrchive.git'
configure_option = ' --prefix='+global_setting.AstroSoft_psrchive

def get_psrchive():
    #get_package.get_package(psrchive_url,psrchive_name,psrchive_size)
    os.chdir(global_setting.AstroSoft_Src)
    #print os.getcwd()
    os.system('git clone '+psrchive_git)

def install_psrchive():
    # Here will install the psrchive
    os.chdir(global_setting.AstroSoft_Src)
    os.system('tar zxvf '+ psrchive_name)
    os.chdir('psrchive')
    os.system('./bootstrap')
    #install_package.install_package(global_setting.AstroSoft_psrchive,psrchive_name,configure_option,4)
    os.system('./configure '+configure_option)
    os.system('make')
    os.system('make install')
def setting_psrchive():
    # Here will setting the psrchive
    pass

if __name__ == '__main__':
    #get_psrchive()
    install_psrchive()
