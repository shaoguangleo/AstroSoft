#!/usr/bin/env python
import platform
import sys
import time
import terminalColor
import support_os
import history
import pgplot
import createDir
import calceph
import psrcat
import tempo
import tempo2
import sigproc
import presto
import psrchive
import dspsr
import preUbuntu

__author__ = "Guo Shaoguang<sgguo@shao.ac.cn>"
__version__ = 1.0
__date__ = "2015-08-18"

delay = 3

''' the format is [['Name','Version','code','arch']]'''
#support_os =['Ubuntu','14.04','trusty','x86_64']
#support_os = support_os.support_os


def check():
    # Here will judge if support OS
    linux_distribution = platform.linux_distribution()
    check_no = 0
    for i  in range(len(linux_distribution)):
        if linux_distribution[i] in support_os[0]:
            check_no = check_no + 1

    if check_no == len(linux_distribution):
        print terminalColor.GREEN
        print '#'*75
        print 'Yes , the installation will start quickly.'
        print '#'*75
        print terminalColor.NONE
    else:
        print terminalColor.RED
        print '#'*75
        print 'Sorry , now the script does not support this OS'
        print 'Of course , you can use -f option to continue.'
        print 'But I am not sure it will work'
        print '#'*75
        print terminalColor.NONE
        sys.exit()

if __name__ == '__main__':
#    history.history()
#    time.sleep(delay)
#    check()
    createDir.createDir()

    print terminalColor.BLINK_GREEN_TEXT_WHITE_BACKGROUND
    print '>>> Now this script will support the following OS and software',
    print terminalColor.NONE

    support_os.show_support_os()

    print terminalColor.BLINK_GREEN_TEXT_WHITE_BACKGROUND
    print '>>> First check if you have install the dependency software',
    print terminalColor.NONE

    preUbuntu.preUbuntu()

    print terminalColor.BLINK_GREEN_TEXT_WHITE_BACKGROUND
    print '>>> Now this installation will start in %d seconds' % delay,
    print terminalColor.NONE

    time.sleep(delay)

    pgplot.install_pgplot()
    print '==  Going to install calceph  ==='
    calceph.install_calceph()
    print '==  Going to install psrcat  ==='
    psrcat.install_psrcat()
    print '==  Going to install tempo  ==='
    tempo.install_tempo()
    print '==  Going to install tempo2  ==='
    tempo2.install_tempo2()
    print '==  Going to install sigproc  ==='
    sigproc.install_sigproc()
    #print '==  Going to install presto  ==='
    #presto.install_presto()
    print '==  Going to install psrchive  ==='
    psrchive.install_psrchive()
    print '==  Going to install dspsr  ==='
    dspsr.install_dspsr()
