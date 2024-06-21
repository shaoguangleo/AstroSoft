FROM shaoguangleo/centos-pgplot:latest
MAINTAINER [Guo Shaoguang] <sgguo@shao.ac.cn>

LABEL version="0.1"
LABEL description="Basic CentOS difmap Image"

COPY src/difmap2.5e.tar.gz /tmp/

WORKDIR /tmp/
RUN yum -y install ncurses-devel && \
	tar zxvf difmap2.5e.tar.gz && \
    cd /tmp/uvf_difmap && \
    sed -i 's/f77/gfortran/g' configure && \
    ./configure linux-ia64-gcc && \
    cp /usr/local/pgplot/libpgplot.a lib/ && \
    ./makeall && \
    cp difmap /usr/local/bin/
