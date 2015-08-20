#!/usr/bin/env python

__author__ = "Guo Shaoguang<sgguo@shao.ac.cn>"
__version__ = 1.0
__date__ = "2015-08-18"

# This file contain the support OS and related software

support_os =[
                ['|','------------------ \t','|','------------------\t','|\n'],
                ['|','System OS          \t','|','Software (Version)\t','|\n'],
                ['|','------------------ \t','|','------------------\t','|\n'],
                ['|','Ubuntu 14.04 x86_64\t','|','pgplot   (5.2)    \t','|\n'],
                ['|','------------------ \t','|','------------------\t','|\n'],
                ['|','Ubuntu 12.04 x86_64\t','|','pgplot   (5.2)    \t','|\n'],
                ['|','------------------ \t','|','------------------\t','|\n']
            ]
def show_support_os():
    for tmp in range(len(support_os)):
        for tmpA in support_os[tmp]:
            print tmpA ,

if __name__ == '__main__':
    show_support_os()
