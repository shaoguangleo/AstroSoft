# About

Dockerfile to build a Rocky [8.6] lastest base image with some useful packages.

The image is built on top of the most recently `Rocky` image and installs the following extra packages:

- `vim`
- `gcc`
- `libX11-devel`
- `gcc-gfortran`

The packages are selected for common use in the future. 

# How to run

Just type the following commands

```
$ docker run -it shaoguangleo/rocky[:version]
```

As we all know, the version can be `lateset` or `$ cat VERSION`

# travis

[![Build Status](https://www.travis-ci.org/shaoguangleo/docker-rocky.svg?branch=master)](https://www.travis-ci.org/shaoguangleo/docker-rocky)
