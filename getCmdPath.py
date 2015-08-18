
#!/usr/bin/env python
import os
# This file will return the path of cmd
__author__ = "Guo Shaoguang<sgguo@shao.ac.cn>"
__version__ = 1.0
__date__ = "2015-08-18"

def getCmdPath(cmd):
    return os.popen('which '+cmd).read().strip('\n')


if __name__ == '__main__':
    print getCmdPath('wget')

