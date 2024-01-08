FROM shaoguangleo/ubuntu-pgplot

LABEL [Guo Shaoguang] <sgguo@shao.ac.cn>

LABEL version="3.23"
LABEL description="Ubuntu HOPS Images"

ENV HOPS_VERSION_FULL=3.23-3383
ENV HOPS_VERSION_ABBR=3.23

SHELL ["/bin/bash", "-c"]

COPY src/* /tmp/

WORKDIR /usr/local/hops/

RUN apt-get update \
    && ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
    && apt-get clean all \
    && rm -rf /var/lib/apt/lists/*

RUN cd /tmp/ \
    && tar zxvf  hops-$HOPS_VERSION_FULL.tar.gz \
    && cd /tmp/hops-$HOPS_VERSION_ABBR \
    && mkdir -p /usr/local/hops \
    && cd /usr/local/hops \
    && /tmp/hops-${HOPS_VERSION_ABBR}/configure 2>&1 | tee log_configure.txt \
    && source  hops.bash \
    && make install 2>&1 | tee log_make_install.txt \
    && echo "source /usr/local/hops/hops.bash" >> ~/.bashrc \
    && cp /tmp/AS_HOPS_logo /usr/local/hops/  \
    && echo "cat /usr/local/hops/AS_HOPS_logo" >> ~/.bashrc \
    && rm -rvf /tmp/*