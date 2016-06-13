#!/usr/bin/env python

# This file will install software
import os
import terminalColor
import global_setting

__author__ = "Guo Shaoguang<sgguo@shao.ac.cn>"
__version__ = 1.0
__date__ = "2015-08-20"
def install_package(package_dest,package_name,configure_option,how_many_jobs):
    # Step:
    os.chdir(global_setting.AstroSoft_Src)
    #     1. tar zvxf filename.tar.gz
    if os.system('tar zxvf '+package_name):
        print 'Unable to tar the %s' % package_name
    #     2. cd filename
    #if os.system('cd '+package_name.split('.tar.gz')[0]):
    #    print 'Unable to enter into %s ' % package_name.split('.tar.gz')[0]
    os.chdir(package_name.split('.tar.gz')[0])
    #     3. ./configure --prefix=/path/install
    if os.system('./configure --prefix='+package_dest+' '+ configure_option):
        print 'Unable to configure %s ' % package_name
    #     4. make -j jobs
    if os.system('make -j '+str(how_many_jobs)):
        print 'Unable to make in %s' % package_name
    #     5. make install
    if os.system('make install'):
        print 'Unable to install %s' % package_name
    #
        print terminalColor.GREEN
        print 'Good job....' + terminalColor.NONE
        return
