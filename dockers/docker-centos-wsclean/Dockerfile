FROM centos:8
LABEL org.opencontainers.image.authors="Shaoguang Guo <sgguo@shao.ac.cn>"

LABEL version="3.2"
LABEL description="CentOS8 WSClean Image"

# Because Centos8 is EOL, we need to use the repos Vault where old things are archived:
RUN \
            sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* && \
            sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

# Enable epel & power tools repositories
RUN yum -y install epel-release dnf-plugins-core && \
            yum config-manager --set-enabled powertools

RUN yum -y install \
            blas-devel \
            boost-devel \
            cfitsio-devel \
            cmake \
            fftw-devel \
            gcc-c++ \
            git \
            gsl-devel \
            hdf5-devel \
            lapack-devel \
            lua-devel \
            make \
            python3 \
            python3-devel \
            libarchive
# Libarchive is not required by wsclean, but because of a RHEL8 issue needs to be manually installed to use cmake
# (See e.g. https://github.com/ComplianceAsCode/content/issues/7016 )

# casacore dependencies & compilation
RUN \
          yum -y install \
             bison \
             bzip2 \
             flex \
             gcc-gfortran \
             ncurses-devel \
             python3-libs \
             readline-devel \
             wcslib-devel \
             wget \
          && \
          mkdir /external && \
          cd /external && \
          git clone https://github.com/casacore/casacore.git && \
          cd /external/casacore && \
          git checkout v3.3.0 && \
          mkdir build && \
          cd build && \
          cmake .. -DBUILD_PYTHON=OFF -DBUILD_TESTING=OFF && \
          make -j`nproc` && \
          make install -j`nproc`

ADD . /src
WORKDIR /src

RUN \
          mkdir /build && \
          cd /build && \
          git clone https://gitlab.com/aroffringa/wsclean.git && \
          cd wsclean && \
          mkdir build && cd build &&\
          cmake .. && \
          make -j`nproc` && \
          make install && \
          && echo "echo '    _      ____     ___    ____  '" >> ~/.bashrc \
          && echo "echo '   / \    / ___|   / _ \  |  _ \ '" >> ~/.bashrc \
          && echo "echo '  / _ \   \___ \  | | | | | | | |'" >> ~/.bashrc \
          && echo "echo ' / ___ \   ___) | | |_| | | |_| |'" >> ~/.bashrc \
          && echo "echo '/_/   \_\ |____/   \___/  |____/ '" >> ~/.bashrc \
          && echo "echo ' '" >> ~/.bashrc \
          && echo "echo 'Details On <https://www.github.com/shaoguangleo/AstroSoft> '" >> ~/.bashrc\
          wsclean --version

