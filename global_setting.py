#!/usr/bin/env python
import os
# This file include the global setting
# You can change the setting free

__author__ = "Guo Shaoguang<sgguo@shao.ac.cn>"
__version__ = 1.0
__date__ = "2015-08-19"

MARK = 'AstroSoft'
HOME_DIR= os.path.expanduser('~')

AstroSoft_Home      = HOME_DIR +'/AstroSoft'
AstroSoft_Src       = AstroSoft_Home+'/src'
AstroSoft_pgplot    = AstroSoft_Home+'/pgplot'
AstroSoft_tempo     = AstroSoft_Home+'/tempo'
AstroSoft_tempo2    = AstroSoft_Home+'/tempo2'
AstroSoft_sigproc   = AstroSoft_Home+'/sigproc'
AstroSoft_presto    = AstroSoft_Home+'/presto'
AstroSoft_psrcat    = AstroSoft_Home+'/psrcat'
AstroSoft_cfitsio   = AstroSoft_Home+'/cfitsio'
AstroSoft_calceph   = AstroSoft_Home+'/calceph'
AstroSoft_psrchive  = AstroSoft_Home+'/psrchive'
AstroSoft_dspsr     = AstroSoft_Home+'/dspsr'

PreUbuntu_software = ('build-essential autoconf automake libtool git cvs swig g++ gfortran python-pip libatlas-* libfftw3-* libcfitsio3* liblapack* python-dev csh')
PrePip_software =('ipython numpy scipy matplotlib')
