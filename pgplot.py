#!/usr/bin/env python

# This file will download pgplot and install it
import os
import terminalColor
import get_cmd_path
import global_setting
import get_package
import substitute
# Changelog
# 2015-08-20

__author__ = "Guo Shaoguang<sgguo@shao.ac.cn>"
__version__ = 1.0
__date__ = "2015-08-18"

# The download url
pgplot52_name = 'pgplot522.tar.gz'
pgplot52_size = 1197397 # here to check if the file completely
pgplot52_url = 'ftp://ftp.astro.caltech.edu/pub/pgplot/'+pgplot52_name

def get_pgplot():
    get_package.get_package(pgplot52_url,pgplot52_name,pgplot52_size)

def install_pgplot():
    # Here will install the pgplot
    os.system('cp drivers.list '+global_setting.AstroSoft_pgplot)
    # os.system('cp makefile_pgplot ' + global_setting.AstroSoft_pgplot+'/makefile_pgplot')
    os.chdir(global_setting.AstroSoft_Src)
    os.system('tar zxvf '+ pgplot52_name)
    os.chdir(global_setting.AstroSoft_pgplot)
    #os.system('wget http://blog.csdn.net/shaoguangleo/article/details/drivers.list');
    os.system(global_setting.AstroSoft_Src+'/pgplot/makemake '+global_setting.AstroSoft_Src + '/pgplot linux g77_gcc_aout')
    substitute.substitute('makefile','makefile_pgplot','FCOMPL=g77','FCOMPL=gfortran\n')
    os.system('cp makefile_pgplot makefile')
    os.system('make')
    os.system('make cpg')
    os.system('make clean')
    print 'DONE'
    #install_package.install_package(global_setting.AstroSoft_psrchive,psrchive_name,configure_option,4)
    pass

def setting_pgplot():
    # Here will setting the pgplot
    pass

if __name__ == '__main__':
    #get_pgplot()
    install_pgplot()
