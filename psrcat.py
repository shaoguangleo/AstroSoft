#!/usr/bin/env python

# This file will download psrcat and install it
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
__date__ = "2015-08-20"

# The download url
psrcat_name= 'psrcat_pkg.tar.gz'
psrcat_name_tar= 'psrcat_tar'
psrcat_size = 9999999# here to check if the file completely
psrcat_url = 'http://54.153.202.3/psrcat/downloads/'+psrcat_name
configure_option = ' '

def get_psrcat():
    get_package.get_package(psrcat_url,psrcat_name,psrcat_size)

def install_psrcat():
    # Here will install the psrcat
    # install_package.install_package(global_setting.AstroSoft_psrcat,psrcat_name,configure_option,4)
    os.chdir(global_setting.AstroSoft_Src)
    if os.system('tar zxvf '+psrcat_name):
        print 'Unable to tar the %s' % psrcat_name
    if os.chdir(psrcat_name_tar):
        print 'Unable to cd %s ' % psrcat_name_tar
    if os.system('source makeit'):
        print 'Unable to makeit - %s ' % psrcat_name_tar
    # here to copy the related (psrcat and psrcat.db) to $AstroSoft/psrcat
    os.system('cp psrcat psrcat.db '+ global_setting.AstroSoft_psrcat)

def setting_psrcat():
    # Here will setting the psrcat
    pass

if __name__ == '__main__':
    #get_psrcat()
    install_psrcat()
