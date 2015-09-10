# This bashrc is just for pulsar toolkit
export ASTROSOFT=~/AstroSoft
export CALCEPH=~/AstroSoft/calceph
export TEMPO=~/AstroSoft/tempo
export TEMPO2=~/AstroSoft/tempo2
export TEMPO2_LIB=$TEMPO2/lib
export TEMPO2_INC=$TEMPO2/include
export PSRCAT_FILE=~/AstroSoft/psrcat/psrcat.db
export PRESTO=~/AstroSoft/presto
export PATH=$PATH:/$PRESTO/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PRESTO/lib:$TEMPO2_LIB
export PYTHONPATH=$PYTHONPATH:$PRESTO/lib/python
export PSRCHIVE=~/AstroSoft/psrchive
export SIGPROC=~/AstroSoft/sigproc

export PGPLOT_DIR=~/AstroSoft/pgplot
export PGPLOT_DEV=/Xserve
export PGPLOT_FONT=~/AstroSoft/pgplot/grfont.dat
export PGPLOT_RGB=~/AstroSoft/pgplot/rgb.txt

export PATH=$PATH:$TEMPO/bin
export PATH=$PATH:$TEMPO2/bin
export PATH=$PATH:$PRESTO/bin
export PATH=$PATH:$PSRCHIVE/bin
export PATH=$PATH:$CALCEPH/bin
export PATH=$PATH:$SIGPROC/bin
