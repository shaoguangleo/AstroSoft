FROM shaoguangleo/ubuntu22.04
LABEL [Guo Shaoguang] <sgguo@shao.ac.cn>

LABEL version="0.1"
LABEL description="HeTu Image based on Ubuntu 22.04"

COPY requirements.txt /tmp/requirements.txt

WORKDIR /usr/local/ai/

RUN apt-get install -y python3-numpy \
    && apt-get install -y python3-requests \
    && apt-get install -y python3-pip \
    && apt-get install -y python3-venv \
    && /usr/bin/python3 -m venv /ai \
    && source /ai/bin/activate \
    && /ai/bin/pip3 install -r /tmp/requirements.txt \
    && apt-get install -y python3-mpi4py
