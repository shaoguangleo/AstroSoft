FROM ubuntu:20.04
MAINTAINER [Guo Shaoguang] <sgguo@shao.ac.cn>

LABEL version="0.1"
LABEL description="Basic Ubuntu Image based on 20.04"


RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y tzdata \
    && apt-get install -y pkg-config \
    && apt-get install -y g++ \
    && apt-get install -y gfortran \
    && apt-get install -y bison \
    && apt-get install -y flex \
    && apt-get install -y libexpat1-dev \
    && apt-get install -y fftw3-dev \
    && apt-get install -y automake \
    && apt-get install -y autoconf \
    && apt-get install -y libtool \
    && apt-get install -y build-essential\
    && apt-get install -y pgplot5 \
    && apt-get install -y subversion \
    && apt-get install -y libgsl-dev \
    && apt-get install -y libopenmpi-dev \
    && apt-get install -y openmpi-bin \
    && apt-get install -y vim \
    && apt-get install -y xorg-dev \
    && apt-get install -y wget \
    && apt-get install -y curl \
    && apt-get install -y git \
    && apt-get install -y cmake \
    && apt-get install -y python python-dev \
    && apt-get install -y rpcbind \
    && apt-get install -y csh \
    && apt-get install -y libglib2.0-dev \
    && apt-get install -y dh-autoreconf\
    && apt-get install -y libcfitsio8 \
    && apt-get install -y libcfitsio-dev \
    && apt-get install -y libpng-dev \
    && apt-get install -y cpio\
    && apt-get install -y libaio-dev\
    && apt-get install -y chrony
