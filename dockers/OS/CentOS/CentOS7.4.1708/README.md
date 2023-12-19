# About

Dockerfile to build a centos[7.4] lastest base image with some useful packages.

The image is built on top of the most recently `centos` image and installs the following extra packages:

- `vim`
- `gcc`
- `libX11-devel`
- `gcc-gfortran`

The packages are selected for common use in the future. 

# How to run

Just type the following commands

```
$ docker run -it shaoguangleo/centos[:version]
```

As we all know, the version can be `lateset` or `$ cat VERSION`

# travis

[![Build Status](https://www.travis-ci.org/shaoguangleo/docker-centos.svg?branch=master)](https://www.travis-ci.org/shaoguangleo/docker-centos)
