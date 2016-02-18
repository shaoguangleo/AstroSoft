#!/usr/bin/env python

# This file will download tempo2 and install it
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
tempo2_name= 'tempo2.tar.gz'
tempo2_size = 9999999# here to check if the file completely
#tempo2_url = 'http://www.imcce.fr/inpop/tempo2/'+tempo2_name
tempo2_git = 'https://bitbucket.org/mkeith/tempo2.git'
configure_option = ' --prefix='+global_setting.AstroSoft_tempo2
#configure_option = ' -L~/AstroSoft/calceph/include --with-calceph='+global_setting.AstroSoft_calceph+'/lib/libcalceph.a'

def get_tempo2():
    #get_package.get_package(tempo2_url,tempo2_name,tempo2_size)
    os.chdir(global_setting.AstroSoft_Src)
    #print os.getcwd()
    os.system('git clone '+tempo2_git)

def install_tempo2():
    # Here will install the tempo2
    os.chdir(global_setting.AstroSoft_Src)
    os.system('tar zxvf '+ tempo2_name)
    os.chdir('tempo2')
    os.system('./bootstrap')
    os.system('cp -r T2runtime '+global_setting.AstroSoft_tempo2)
    #install_package.install_package(global_setting.AstroSoft_tempo2,tempo2_name,configure_option,4)
    os.system('./configure '+configure_option)
    os.system('make')
    os.system('make install')
    # Do not know should we enter the plugins directory
    os.system('make plugins')
    os.system('make plugins-install')
    # Here to copy some needed files
def setting_tempo2():
    # Here will setting the tempo2
    pass

if __name__ == '__main__':
    #get_tempo2()
    install_tempo2()
