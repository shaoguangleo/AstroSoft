FROM shaoguangleo/ubuntu20.04
LABEL [Guo Shaoguang] <sgguo@shao.ac.cn>

LABEL version="1.0"
LABEL description="Basic Ubuntu PGPLOT Image"

COPY src/* /usr/local/src/

WORKDIR /usr/local/src/
RUN tar zxvf pgplot5.2.tar.gz && \
    mkdir /usr/local/pgplot && \
    cd /usr/local/pgplot && \
    cp /usr/local/src/drivers.list . &&\
    /usr/local/src/pgplot/makemake /usr/local/src/pgplot linux g77_gcc_aout && \
    cat makefile | sed "s;g77;gfortran;g" > makefile.new &&\
    rm makefile && \
    mv makefile.new makefile && \
    cat makefile | sed "s;FFLAGD=-fno-backslash;FFLAGD=-fno-backslash -fPIC;g" > makefile.new &&\
    rm makefile && \
    mv makefile.new makefile && \
    cat makefile | sed "s;FFLAGC=-Wall -O;FFLAGC=-ffixed-form -ffixed-line-length-none -u -Wall -O -fPIC;g" > makefile.new &&\
    rm makefile && \
    mv makefile.new makefile && \
    cat makefile | sed "s;CFLAGC=-DPG_PPU -O2 -I.;CFLAGC=-DPG_PPU -O2 -I. -fPIC;g" > makefile.new &&\
    rm makefile && \
    mv makefile.new makefile && \
    make && \
    make cpg && \
    make clean && \
    echo "export PGPLOT_DIR=/usr/local/pgplot" >> ~/.bashrc && \
    echo "export PGPLOT_DEV=/Xserve" >> ~/.bashrc && \
    cp /usr/local/src/AS_PG_logo /usr/local/pgplot/ && \
    echo "cat /usr/local/pgplot/AS_PG_logo" >> ~/.bashrc

