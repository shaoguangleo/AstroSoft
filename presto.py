#!/usr/bin/env python

# This file will download presto and install it
import os
import terminalColor
import global_setting
import get_package
import install_package
# Changelog
# 2015-08-20

__author__ = "Guo Shaoguang<sgguo@shao.ac.cn>"
__version__ = 1.0
__date__ = "2015-08-18"

# The download url
presto_name= 'presto.tar.gz'
presto_size = 9999999# here to check if the file completely
#presto_url = 'http://www.imcce.fr/inpop/presto/'+presto_name
presto_git = 'git://github.com/scottransom/presto.git'
configure_option = ' '

def get_presto():
    #get_package.get_package(presto_url,presto_name,presto_size)
    os.chdir(global_setting.AstroSoft_Src)
    #print os.getcwd()
    os.system('git clone '+presto_git)

def install_presto():
    # Here will install the presto
    os.chdir(global_setting.AstroSoft_Src)
    os.system('tar zxvf '+ presto_name)
    os.chdir('presto/src')
    #install_package.install_package(global_setting.AstroSoft_presto,presto_name,configure_option,4)
    os.system('make makewisdom')
    os.system('make prep')
    os.system('make')
    os.system('make install')
def setting_presto():
    # Here will setting the presto
    pass

if __name__ == '__main__':
    #get_presto()
    install_presto()
