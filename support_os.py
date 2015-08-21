#!/usr/bin/env python

__author__ = "Guo Shaoguang<sgguo@shao.ac.cn>"
__version__ = 1.0
__date__ = "2015-08-18"

# This file contain the support OS and related software

support_os =[
                ['|','------------------ \t','|','------------------\t','|\n'],
                ['|','System OS          \t','|','Software (Version)\t','|\n'],
                ['|','------------------ \t','|','------------------\t','|\n'],
                ['|','Ubuntu 12.04 x86_64\t','|','pgplot   (5.2)    \t','|\n'],
                ['|','                   \t','|','calceph  (2.2.3)    \t','|\n'],
                ['|','                   \t','|','psrcat   (x.x)    \t','|\n'],
                ['|','                   \t','|','tempo    (x.x)    \t','|\n'],
                ['|','                   \t','|','tempo2   (x.x)    \t','|\n'],
                ['|','                   \t','|','sigproc  (x.x)    \t','|\n'],
                #['|','                   \t','|','presto   (x.x)    \t','|\n'],
                ['|','                   \t','|','psrchive (2012-12+)\t','|\n'],
                ['|','                   \t','|','dspsr    (2.0)    \t','|\n'],
                ['|','------------------ \t','|','------------------\t','|\n'],
                ['|','MacOSX 10.10.4 x86_64\t','|','pgplot   (5.2)    \t','|\n'],
                ['|',' OS X Yosemite       \t','|','calceph  (2.2.3)    \t','|\n'],
                ['|','                   \t','|','psrcat   (x.x)    \t','|\n'],
                ['|','                   \t','|','tempo    (x.x)    \t','|\n'],
                #['|','                   \t','|','tempo2   (x.x)    \t','|\n'],
                #['|','                   \t','|','sigproc  (x.x)    \t','|\n'],
                #['|','                   \t','|','presto   (x.x)    \t','|\n'],
                ['|','                   \t','|','psrchive (2012-12+)\t','|\n'],
                ['|','                   \t','|','dspsr    (2.0)    \t','|\n'],
                ['|','------------------ \t','|','------------------\t','|\n']
            ]
def show_support_os():
    for tmp in range(len(support_os)):
        for tmpA in support_os[tmp]:
            print tmpA ,

if __name__ == '__main__':
    show_support_os()
