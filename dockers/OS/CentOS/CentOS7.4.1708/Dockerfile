FROM centos:7.4.1708
MAINTAINER [Guo Shaoguang] <sgguo@shao.ac.cn>

LABEL version="0.1"
LABEL description="Base CentOS Image"

COPY src/fftw-3.3.8.tar.gz /tmp/

RUN yum update -y \
    && yum upgrade -y \
    && yum install -y vim \
    && yum install -y gcc \
    && yum install -y gcc-c++ \
    && yum install -y make \
    && yum install -y git \
    && yum install -y epel-release \
    && yum install -y libX11-devel\
    && yum install -y gcc-gfortran\
    && yum install -y subversion\
    && yum install -y pkgconfig\
    && yum install -y bison\
    && yum install -y flex\
    && yum install -y fftw fftw-devel\
    && cd /tmp \
    && tar zxvf fftw-3.3.8.tar.gz \
    && cd /tmp/fftw-3.3.8 \
    && ./configure --enable-shared --enable-threads --enable-float CFLAGS=-fPIC FFLAGS=-fPIC\
    && make -j 2\
    && make install\
    && make clean\
    && ./configure --enable-shared --enable-threads --enable-long-double CFLAGS=-fPIC FFLAGS=-fPIC\
    && make -j 4\
    && make install\
    && make clean\
    && ./configure --enable-sse2 --enable-avx\
    && make -j 4\
    && make install\
    && make clean\
    && yum install -y glib glib-devel\
    && yum install -y glib2 glib2-devel\
    && yum install -y cfitsio cfitsio-devel\
    && yum install -y libpng libpng-devel\
    && yum install -y wget\
    && yum install -y openmpi\
    && yum install -y openmpi-devel\
    && yum install -y mpich-3.2\
    && yum install -y mpich-3.2-devel\
    && yum install -y libtool*\
    && yum install -y automake\
    && yum install -y cmake\
    && yum install -y cmake3\
    && yum install -y boost\
    && yum install -y autoconf\
    && yum install -y expat\
    && yum install -y expat-devel\
    && yum install -y python\
    && yum install -y python-devel\
    && yum install -y ipython\
    && yum install -y python34-pip python2-pip \
    && yum install -y rpcbind\
    && yum install -y tcsh\
    && yum install -y numpy numpy-f2py scipy\
    && export PATH=$PATH:/usr/lib64/mpich-3.2/bin/\
    && echo "export PATH=$PATH:/usr/lib64/mpich-3.2/bin/" >> ~/.bashrc\
    && rm -rf /var/lib/yum/yumdb/*
