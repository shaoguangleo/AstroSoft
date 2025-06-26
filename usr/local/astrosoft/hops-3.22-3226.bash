#!/bin/sh
#
# (Ba)sh startup
#
# $Id: hops.bash.in 3202 2021-03-03 22:09:44Z barrettj $
#
# Version 3.22
#

#
# Help for the befuddled user.  The name is probably hops.bash.
#
zero=hops.bash
Help='Usage: . /usr/local/astrosoft/hops-3.22-3226/bin/'$zero'

will set up your HOPS environment by modifying the following variables:

    PATH            executable search path
    INFOPATH        info file search path
    LD_LIBRARY_PATH adds dynamic linkage to PGPLOT_DIR
    PYTHONPATH      for a few useful python tools

    HOPS_ROOT       root of the HOPS package
    HOPS_VERS       version number of this package
    HOPS_ARCH       installation architecture
    HOPS_DOCS       program documentation support
    HOPS_SETUP      is set true after invocation
    HOPS_QUIET      controls setup diagnostics
    HOPS_PREFIX     directory where hops was installed

    PGPLOT_DIR      sets this appropriately if not otherwise defined
    PGPLOT_TYPE     sets this to /xw if not defined
    PGPLOT_DEV      sets this to /xw if not defined
    PGPLOT_FONT     may be set to location of grfont.dat
    PGPLOT_RGB      may be set to location of rgb.txt
    PROGDOC         used by HOPS vhelp to find help texts
    TEXT            used by HOPS for text configuration files
    AHELP           used by aedit for help texts
    DEF_CONTROL     used by fourfit
    GS_DEVICE       used by ghostscript
    DATADIR         parent of experiment data directory
    TESTDATADIR     directory for hops test data

    SCHEDDIR, AFILEDIR, SYSVEX, TASK, BIN, TMP
		    heritage variables that are
		    assigned but perhaps not used

    MK4_PRINTER	    can be pointed to your preferred printer

Set HOPS_QUIET (to anything) if you do not want the chatter.
Once setup, HOPS_SETUP is defined to be "true".  You can set this
to "false" to reinitialize with a different version of the software,
e.g. something like one of these (depending on which '$zero')

    HOPS_SETUP=false . ~/bin/'$zero'
    HOPS_SETUP=false . /usr/local/astrosoft/hops-3.22-3226/'$zero'

Otherwise, reinvocation will merely tell you what you are using.
To purge HOPS from your environment, set HOPS_SETUP to "purge".
'
Version="./$zero  [ 2025-06-26T05:40:15 ]"
case "nada$1" in
nada--help)     echo "$Help"    ; exit 0 ;;
nada--version)  echo "$Version" ; exit 0 ;;
nada)                                    ;;
nada*)          echo "$Help"    ; exit 1 ;;
esac

#
# remove old version from PATH
#
[ -n "$HOPS_SETUP" -a -n "$HOPS_ROOT" ] && {
  [ "$HOPS_SETUP" = true ] || {
    [ -z "$HOPS_QUIET" ] && echo Revising HOPS version.
    prefix=$hops_prefix
    [ -z "$prefix" ] && prefix=/usr/local/astrosoft/hops-3.22-3226
    exec_prefix=$hops_exec_prefix
    [ -z "$exec_prefix" ] && exec_prefix=${prefix}
    datarootdir=$hops_datarootdir
    [ -z "$datarootdir" ] && datarootdir=${prefix}/share
    pythondir=$hops_pythondir
    [ -z "$pythondir" ] && pythondir=${prefix}/lib/python3.12/site-packages
    Path=`echo $PATH | sed -e "s+${exec_prefix}/bin[:]*++g"`
    Info=`echo $INFOPATH | sed -e "s+${datarootdir}/info[:]*++g"`
    Libp=`echo $LD_LIBRARY_PATH | sed -e "s+${exec_prefix}/lib/hops[:]*++g"`
    Pyp=`echo $PYTHONPATH | sed -e "s+${pythondir}/hops[:]*++g"`
    Pyp=`echo $Pyp | sed -e "s+${pythondir}[:]*++g"`
    export PATH=$Path
    export INFOPATH=$Info
    export LD_LIBRARY_PATH=$Libp
    export PYTHONPATH=$Pyp
    [ "$HOPS_SETUP" = false ] && HOPS_SETUP=''
    unset HOPS_ROOT HOPS_VERS HOPS_ARCH HOPS_DOCS HOPS_PREFIX
    unset PROGDOC TEXT AHELP DEF_CONTROL DATADIR TESTDATADIR
    unset SCHEDDIR AFILEDIR SYSVEX TASK BIN TMP
    unset PGPLOT_DIR PGPLOT_TYPE PGPLOT_DEV PGPLOT_FONT PGPLOT_RGB
    unset prefix exec_prefix datarootdir pythondir
    unset Path Info Libp Pyp
  }
}

# using variables as defined by config.status where possible
# datarootdir is required for autoconf 2.6 and later
[ -z "$prefix" ] && prefix=/usr/local/astrosoft/hops-3.22-3226
[ -z "$exec_prefix" ] && exec_prefix=${prefix}
[ -z "$datarootdir" ] && datarootdir=${prefix}/share
[ -z "$pythondir" ] && pythondir=${prefix}/lib/python3.12/site-packages
hops_prefix=$prefix
hops_exec_prefix=$exec_prefix
hops_datarootdir=$datarootdir
hops_pythondir=$pythondir

[ -z "$HOPS_SETUP" ] && {
    #
    # basic stuff
    #
    Setup=Setup
    export HOPS_ROOT=/usr/local/astrosoft/src
    export HOPS_PREFIX=/usr/local/astrosoft/hops-3.22-3226
    export HOPS_ARCH=x86_64-3.22
    export HOPS_VERS=3.22
    export HOPS_SETUP=true

    Path=${exec_prefix}/bin
    [ -z "$PATH" ] && PATH=${Path} || PATH=${Path}:$PATH

    Info=${datarootdir}/info
    [ -z "$INFOPATH" ] && INFOPATH=${Info} || INFOPATH=${Info}:$INFOPATH
    export INFOPATH

    [ -z "$PGPLOT_DIR" ] && Libp=/usr/local/astrosoft/pgplot || Libp=$PGPLOT_DIR
    export PGPLOT_DIR=$Libp

    [ -z "$PGPLOT_TYPE" ] && PGPLOT_TYPE=/xw
    [ -z "$PGPLOT_DEV" ] && PGPLOT_DEV=/xw
    export PGPLOT_TYPE PGPLOT_DEV

    [ -z "$LD_LIBRARY_PATH" ] && LD_LIBRARY_PATH=$Libp ||
	LD_LIBRARY_PATH=${Libp}:$LD_LIBRARY_PATH
    [ -d "" ] &&
	LD_LIBRARY_PATH=:$LD_LIBRARY_PATH
    LD_LIBRARY_PATH=${exec_prefix}/lib/hops:$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH

    [ -z "$PYTHONPATH" ] && PYTHONPATH=${pythondir}/hops ||
        PYTHONPATH=${pythondir}/hops:$PYTHONPATH
    export PYTHONPATH=$pythondir:$PYTHONPATH

    # program documentation
    export HOPS_DOCS=${datarootdir}/hops
    export PROGDOC=$HOPS_DOCS/vhelp
    export AHELP=$HOPS_DOCS/vhelp/aedit
    export TEXT=$HOPS_DOCS/text

    # miscellany
    [ -z "$DEF_CONTROL" ] && export DEF_CONTROL=/dev/null
    [ -z "$GS_DEVICE" ] && export GS_DEVICE=x11
    [ -z "$PGPLOT_TYPE" ] && export PGPLOT_TYPE=/xw
    [ -n "" ] && export PGPLOT_FONT=
    [ -n "" ] && export PGPLOT_RGB=

    # /correlator/data is the current working equivalent
    [ -z "$DATADIR" ] && export DATADIR=$HOPS_ROOT/data
    [ -z "$TESTDATADIR" ] && export TESTDATADIR=${datarootdir}/hops/testdata

    # printing via autoconfig
    [ -n "" -a -z "$MK4_PRINTER" ] && export MK4_PRINTER=

    # heritage variables that are repointed away from /correlator
    export SCHEDDIR=HOPS-no-such-dir-sched
    export AFILEDIR=HOPS-no-such-dir-afile
    export SYSVEX=HOPS-no-such-dir-sysvex
    export TASK=HOPS-no-such-dir-task
    export BIN=${exec_prefix}/bin
    export TMP=/tmp

    true
} || {
    #
    # basic stuff
    #
    Setup=Using
}

[ -z "$HOPS_QUIET" ] &&
    echo $Setup HOPS v$HOPS_VERS with HOPS_ROOT=$HOPS_ROOT for $HOPS_ARCH

#
# all done
#
unset Path Info Libp Pyp Setup Help Version
unset prefix exec_prefix datarootdir pythondir

#
# eof
#
