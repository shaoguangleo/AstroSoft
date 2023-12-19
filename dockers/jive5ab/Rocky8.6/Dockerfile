FROM shaoguangleo/rocky:latest
MAINTAINER [Guo Shaoguang] <sgguo@shao.ac.cn>

LABEL version="0.1"
LABEL description="Jive5ab image based on Rocky Image"

COPY src/jive5ab-3.2.0.tar.gz /usr/local/src/

WORKDIR /usr/local/src/
RUN cd /usr/local/src/ && \
    tar zxvf jive5ab-3.2.0.tar.gz && \
    cd jive5ab-3.2.0 && \
    mkdir build && \
    cd build && \
    cmake3 .. -DSSAPI_ROOT=nossapi && \
    make -j 8 && \
    make install \
    && echo "echo '    _      ____     ___    ____  '" >> ~/.bashrc \
    && echo "echo '   / \    / ___|   / _ \  |  _ \ '" >> ~/.bashrc \
    && echo "echo '  / _ \   \___ \  | | | | | | | |'" >> ~/.bashrc \
    && echo "echo ' / ___ \   ___) | | |_| | | |_| |'" >> ~/.bashrc \
    && echo "echo '/_/   \_\ |____/   \___/  |____/ '" >> ~/.bashrc \
    && echo "echo ' '" >> ~/.bashrc \
    && echo "echo 'Details On <https://www.github.com/shaoguangleo/AstroSoft> '" >> ~/.bashrc \
    && rm -rvf /tmp/*
