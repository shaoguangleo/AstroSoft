#!/usr/bin/env python

# This file will download tempo and install it
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
tempo_name= 'tempo.tar.gz'
tempo_size = 9999999# here to check if the file completely
#tempo_url = 'http://www.imcce.fr/inpop/tempo/'+tempo_name
tempo_git = 'git://github.com/nanograv/tempo.git'
configure_option = ' '

def get_tempo():
    #get_package.get_package(tempo_url,tempo_name,tempo_size)
    os.chdir(global_setting.AstroSoft_Src)
    #print os.getcwd()
    os.system('git clone '+tempo_git)

def install_tempo():
    # Here will install the tempo
    os.chdir(global_setting.AstroSoft_Src)
    os.system('tar zxvf '+ tempo_name)
    os.chdir('tempo')
    os.system('./prepare')
    install_package.install_package(global_setting.AstroSoft_tempo,tempo_name,configure_option,4)
    # Here to copy some needed files
    os.system('cp -rv clock ephem tzpar util '+global_setting.AstroSoft_tempo)
    # Here to copy the tempo.hlp to $TEMPO
    os.system('cp tempo.hlp '+global_setting.AstroSoft_tempo)
def setting_tempo():
    # Here will setting the tempo
    pass

if __name__ == '__main__':
    #get_tempo()
    install_tempo()
