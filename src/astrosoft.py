#!/usr/bin/env python
# coding=utf-8
import sys
import os
import shao_color

__version__ = "v0.1"
__author__ = 'Guo Shaoguang <sgguo@shao.ac.cn>'
__date__ = '201807'
__name__ = 'ASTROSOFT'

quiet_flag = ''
quiet_mode = ''
quiet_wget = ''
virutal = 0
uninstall = 0
astrosoft_dir = os.environ['ASTROSOFT_DIR']
astrosoft_usr = os.environ['ASTROSOFT_USR']
pkg_idx_ext = os.environ['ASTROSOFT_TREE']

def help():
    print ("USAGE : ")
    print ("    astrosoft package-name {options}")
    print ("")
    print ("    --search        \t do a grep for package")
    print ("    --stable        \t install the latest stable version")
    print ("    --testing       \t install the latest testing version")
    print ("    --devel         \t try and get the devel version")
    print ("    --quiet         \t reduce output")
    print ("    --quieter       \t reduce output even more" )
    print ("    --rebuild       \t remake dependancies even if they are up-to-date")
    print ("    --no-[pkg]      \t build without optional package pkg")
    print ("    --uninstall     \t remove package; be careful of dependancies")
    print ("    --virutal       \t donot actualy install, just mark package as installed")
    print ("    --clear-cache   \t remove cached package install files")
    print ("    --old           \t do not update hte package index (update by default)")
    print ("    --selfupdate    \t update the astrosoft software then exit")
    print ("")
    print ("    Special Packages:")
    print ("    world           \t All installed packages")
    print ("    dirty           \t Packages who's dependancies have been updated since install")
    sys.exit(1)


def welcome():
    print ('#' * 50)
    print ("#    Author  : {0}".format(__author__))
    print ("#    Version : {0}".format(__version__))
    print ("#    Date    : {0}".format(__date__))
    print ('#' * 50)
    print ("")


def setup_enviroment():
    global quiet_flag
    quiet_flag = ''
    global quiet_mode
    quiet_mode = ''
    global quiet_wget
    quiet_wget = ''
    global virutal
    virutal = 0
    global uninstall
    uninstall = 0
    global astrosoft_dir 
    astrosoft_dir = os.environ['ASTROSOFT_DIR']
    global astrosoft_usr
    astrosoft_usr = os.environ['ASTROSOFT_USR']
    global astrosoft_ext 
    astrosoft_ext = os.environ['ASTROSOFT_TREE']

def read_pkg_idx(pkg_index):
    file=open(pkg_index)
    pkgs=dict()
    for line in file:
        elems=line.split();
        if len(elems) > 3:
            pkgs[elems[0]] = dict(name=elems[0], version=elems[1], date=elems[2], url=elems[3])
    file.close()
    return pkgs

def main():
    welcome()
    setup_enviroment()
    color = shao_color.Colored()

    ## Create the struct of astrosoft

    if os.path.exists(astrosoft_dir + '/pkg_files'):
        os.chdir(astrosoft_dir + '/pkg_files')
    else:
        os.mkdir(astrosoft_dir + '/pkg_files')

    if os.path.exists(astrosoft_dir + '/bin'):
        os.chdir(astrosoft_dir + '/bin')
    else:
        os.mkdir(astrosoft_dir + '/bin')
    
    print (os.path.curdir)
    #print ('cp astrosoft-update-index ' + astrosoft_dir + '/bin/')
    #os.system('cp astrosoft-update-index ' + astrosoft_dir + '/bin/')

    if len(sys.argv) < 2 :
        help()


    pkg_search = list()
    upgrade_only = 1
    clear_cache = 0
    yesyesyes = 0
    selfupdate = 0
    updateidx = 1
    ignore_dirty = 0
    make_dirty = 0
    search = 0
    opt_out = list()
    global pkg_idx_ext

    for arg in sys.argv[1:]:
        if arg == '--help':
            help()
        if arg.startswith('--no-'):
            opt_out.append(arg[5:])
        if arg == '--uninstall':
            uninstall = 1
        if arg == '--search':
            search = 1
        if arg == '--rebuild':
            upgrade_only = 0
        if arg == '--upgrade':
            upgrade_only = 1
        if arg == '--mark-dirty':
            make_dirty = 1
        if arg == '--selfupdate':
            selfupdate = 1
        if arg == '--yes':
            yesyesyes = 1
        if arg == '--old':
            updateidx = 0
        if arg == '--clear-cache':
            clear_cache = 1
        if arg == '--ignore_dirty':
            ignore_dirty = 1
        if arg == '--stable':
            pkg_idx_ext = 'stable'
        if arg == '--testing':
            pkg_idx_ext = 'testing'
        if arg == '--devel':
            pkg_idx_ext = 'devel'
        if arg == '--quiet':
            quiet_flag = ' > /dev/null'
            quiet_mode = 'quietly'
        if arg == '--quieter':
            quiet_wget = '-q'
            quiet_flag = ' >& /dev/null'
            quiet_mode = 'very quietly'
        if not arg.startswith('-'):
            pkg_search.append(arg)



    print ('===  {0} {1}  ==='.format(__name__, __version__))
    if pkg_idx_ext == 'stable':
        print (" Package Index : " + color.green('Stable'))
    if pkg_idx_ext == 'testing':
        print (" Package Index : " + color.fuchsia('Testing'))
    if pkg_idx_ext == 'devel':
        print (" Package Index : " + color.red('Devel'))
    print ('='*24)

    if clear_cache:
        print ('Clearing package install cache')
        cmd = 'rm -f ' + astrosoft_dir + '/pkg_files/*'
        print (cmd)
        os.system(cmd)
        sys.exit(0)

    if updateidx:
        print ('Updating package index')
        #os.system(astrosoft_dir + '/bin/astrosoft-update-index')
        os.system('astrosoft-update-index' )
    else:
        print ('Using old package index (maybe out of date !!!)')

    if selfupdate:
        print ('Updating astrosoft software')
        os.system('astrosoft-selfupdate')
        sys.exit(0)

    curr_pkg  = read_pkg_idx(astrosoft_usr + '/var/astrosoft/installed.pkg')
    dirty_pkg = read_pkg_idx(astrosoft_usr + '/var/astrosoft/dirty.pkg') 

    pkg_index_file = 'pkg_indx.%s'%(pkg_idx_ext)

    pkgs = read_pkg_idx(astrosoft_dir + '/' + pkg_index_file)

    ipkg = list()

    

    pass

main()

if __name__ == '__main__':
    main()
