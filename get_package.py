#!/usr/bin/env python

# This file will download pgplot and install it
import os
import terminalColor
import getCmdPath
import globalSetting

__author__ = "Guo Shaoguang<sgguo@shao.ac.cn>"
__version__ = 1.0
__date__ = "2015-08-20"
def get_package(package_url,package_name,package_size):
    if os.path.exists(globalSetting.AstroSoft_Src+package_name):
        if os.path.getsize(globalSetting.AstroSoft_Src+package_name == package_size):
            print '<<<You have download the pgplot package @ %s' % globalSetting.AstroSoft_Src
        else:
            os.system('rm '+globalSetting.AstroSoft_Src+package_name)
    else:
        print terminalColor.BLINK_GREEN_TEXT_WHITE_BACKGROUND
        print 'Now downloading PGPLOT 5.2' + terminalColor.NONE
        # First change the destination directory
        os.chdir(globalSetting.AstroSoft_Src)
        if(os.system(getCmdPath.getCmdPath('wget')+ ' '+ package_url)):
            print ''
            print terminalColor.RED
            print '!!! Make sure you have connect the internet'
            print '!!! It seem that the download is not complete',
            print terminalColor.NONE
            print ''
        print terminalColor.GREEN
        if os.path.exists(globalSetting.AstroSoft_Src+package_name) and (os.path.getsize(globalSetting.AstroSoft_Src+package_name) == package_size):
            print 'Download '+ package_name + ' successfule .' + terminalColor.NONE
        return
