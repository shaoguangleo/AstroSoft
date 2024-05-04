FROM shaoguangleo/ubuntu22.04:latest
LABEL maintainer="sgguo@shao.ac.cn"

LABEL version="0.1"
LABEL description="Basic Ubuntu Miriad Image"

COPY src/miriad-common.tar.bz2 /usr/local/astrosoft/
COPY src/miriad-code.tar.bz2 /usr/local/astrosoft/
COPY src/miriad-linux64.tar.bz2 /usr/local/astrosoft/
COPY as_logo /usr/local/astrosoft/

SHELL ["/bin/bash", "-c"]

WORKDIR /usr/local/astrosoft/
RUN apt -y install libncurses-dev && \
	tar xvf miriad-common.tar.bz2 && \
    tar xvf miriad-code.tar.bz2 && \
    tar xvf miriad-linux64.tar.bz2 && \
    export MIR=/usr/local/astrosoft/miriad && \
    cd /usr/local/astrosoft/miriad && \
    sed -e "s,@MIRROOT@,$MIR," scripts/MIRRC.in > MIRRC && \
    sed -e "s,@MIRROOT@,$MIR," scripts/MIRRC.sh.in > MIRRC.sh && \
    source MIRRC.sh && \
    echo "source $MIR/MIRRC.sh"  >> ~/.bashrc && \
    export PATH=$MIRBIN:$PATH && \
    echo "export PATH=$MIRBIN:$PATH" >> ~/.bashrc && \
    echo "cat /usr/local/astrosoft/as_logo" >> ~/.bashrc && \
    rm /usr/local/astrosoft/*.tar.bz2
