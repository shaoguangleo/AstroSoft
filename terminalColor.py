#!/usr/bin/env python
#-*-coding:utf-8-*-
#Filename: This file will add some color text in the terminal

__author__ = "Guo Shaoguang<sgguo@shao.ac.cn>"
__version__ = 1.0
__date__ = "2015-08-18"

"""
attr#
    0  All attributes off  # default
    1  Bold (or Bright) 粗体 or 高亮
    4  Underline 下划线
    5  Blink 闪烁
    7  Invert 反显
foretext#
    30 Black text
    31 Red text
    32 Green text
    33 Yellow text
    34 Blue text
    35 Purple text
    36 Cyan text
    37 White text
backgroud#
    40 Black background
    41 Red background
    42 Green background
    43 Yellow background
    44 Blue background
    45 Purple background
    46 Cyan background
    47 White background
    """

##Note the setting will be \x1B[%d;%d;%dm % (attr,foretext,background)
NONE    =   '\033[0m'
RED     =   '\033[1;31;47m'
GREEN   =   '\033[1;32;47m'


def test():
    """ """
    for attr in [0,1,4,5,7]:
        print "attribute %d ------------------------------" % (attr)
        for fore in [30,31,32,33,34,35,36,37]:
            for back in [40,41,42,43,44,45,46,47]:
                color = "\x1B[%d;%d;%dm" % (attr,fore,back)
                print "%s %d-%d-%d\x1B[0m" % (color,attr,fore,back),
		print ""
if __name__ == "__main__":
    """ """
    test()
