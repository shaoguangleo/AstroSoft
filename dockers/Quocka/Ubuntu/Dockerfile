FROM shaoguangleo/ubuntu-miriad:latest
LABEL maintainer="sgguo@shao.ac.cn"

LABEL version="0.1"
LABEL description="Ubuntu QUOCKA Image"

COPY as_logo /usr/local/astrosoft/

SHELL ["/bin/bash", "-c"]

WORKDIR /usr/local/astrosoft/
RUN apt install -y ghostscript && \
    git clone https://github.com/AlecThomson/quocka.git && \
    cd quocka && \
    pip install .  -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install fitscube -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --index-url=https://go.nrao.edu/pypi casadata
