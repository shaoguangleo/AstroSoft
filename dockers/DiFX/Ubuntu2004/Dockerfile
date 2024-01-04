FROM ubuntu:20.04

LABEL [Guo Shaoguang & Xu Zhijun] <sgguo@shao.ac.cn & xuthus@shao.ac.cn>

LABEL version="2.8.1"
LABEL description="Ubuntu DiFX Images"

ENV DIFX_VERSION_NO_281=2.8.1
ENV DIFX_VERSION_NO_LATEST=2.8.1

SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
ENV LD_LIBRARY_PATH=/usr/local/difx/$DIFX_VERSION_NO_281/lib
ENV IPPROOT=/opt/intel
ENV PATH=${PATH}:/usr/local/difx/$DIFX_VERSION_NO_281/bin
ENV MPICH_VERSION=3.2.1
#ENV PERL5LIB=/difx/DiFX-2.8.1/share/perl/5.30.0:/difx/DiFX-2.8.1/./lib/x86_64-linux-gnu/perl/5.30.0

COPY src/* /tmp/

WORKDIR /usr/local/difx/

RUN apt-get update \
    && apt-get install -y \
        tzdata \
        autoconf \
        automake \
        libtool \
        pkg-config \
        g++ \
        gcc \
        gfortran \
        make \
        python3 \
        python3-pip \
        libgsl23 \
        libgsl-dev \
        libexpat1-dev \
        bison \
        doxygen \
        python3-tk \
        vim \
        openssh-client \
        libfftw3-dev \
        build-essential \
        autotools-dev \
        flex \
        subversion \
    && ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
    && apt-get clean all \
    && rm -rf /var/lib/apt/lists/*

#ENV TZ=UTC
#ENV TZ=Asia/Shanghai
RUN pip3 install astropy requests numpy simplejson psutil matplotlib

RUN cd /tmp/ \
    && tar zxvf  mpich-$MPICH_VERSION.tar.gz \
    && cd /tmp/mpich-$MPICH_VERSION \
    && ./configure 2>&1 | tee log_configure.txt \
    && make 2>&1 | tee log_make.txt \
    && make install 2>&1 | tee log_make_install.txt \
    && cd /tmp/ \
    && cp /tmp/setup.bash.v$DIFX_VERSION_NO_281 /usr/local/difx/setup.bash.v$DIFX_VERSION_NO_281 \
    && sh l_ipp_oneapi_p_2021.7.0.25396_offline.sh  -a -s --eula accept\
    && tar zxvf  DiFX-${DIFX_VERSION_NO_281}.tar.gz \
    && cd /tmp/DiFX-${DIFX_VERSION_NO_281} \
    && mkdir /usr/local/difx/$DIFX_VERSION_NO_281 \
    && export DIFXROOT=/usr/local/difx/$DIFX_VERSION_NO_281 \
    && source /usr/local/difx/setup.bash.v$DIFX_VERSION_NO_281 \
    && ./install-difx \
    && ./install-difx --doonly=difx2mark4 \
    && echo "source /usr/local/difx/setup.bash.v$DIFX_VERSION_NO_LATEST" >> ~/.bashrc \
    && rm -rvf /tmp/*

