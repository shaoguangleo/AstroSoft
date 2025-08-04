FROM --platform=linux/x86_64 rockylinux/rockylinux:8.6
MAINTAINER [Guo Shaoguang] <sgguo@shao.ac.cn>

LABEL version="0.1"
LABEL description="Base Rocky 8.6 Image"

#COPY src/fftw-3.3.8.tar.gz /tmp/

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
    && yum install -y epel-release\
    && yum install -y fftw fftw-devel\
    && yum install -y glib2 glib2-devel\
    && yum install -y cfitsio cfitsio-devel\
    && yum install -y libpng libpng-devel\
    && yum install -y wget\
    && yum install -y openmpi\
    && yum install -y openmpi-devel\
    && yum install -y mpich \
    && yum install -y mpich-devel\
    && yum install -y libtool*\
    && yum install -y automake\
    && yum install -y cmake\
    && yum install -y boost\
    && yum install -y autoconf\
    && yum install -y expat\
    && yum install -y expat-devel
