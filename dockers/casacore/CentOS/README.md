# About

Dockerfile to build a casacore image based on CentOS.

Read more on casacore offical website on https://www.github.com/casacore/casacore.git now.

# How to run

Just type the following commands

```
$ docker run -it -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix shaoguangleo/centos-casacore
```

As we all know, the version can be `latest` or `$ cat VERSION`

# travis

[![Build Status](https://www.travis-ci.org/shaoguangleo/AstroSoft.svg?branch=master)](https://www.travis-ci.org/shaoguangleo/AstroSoft)
