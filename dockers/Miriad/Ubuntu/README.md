# About

Dockerfile to build a Miriad image based on Ubuntu2204.

## How to run

Just type the following commands

```
$ docker run -it -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix shaoguangleo/ubuntu-miriad
#or MacOSX

$docker run -it -e DISPLAY=host.docker.internal:0 shaoguangleo/ubuntu-miriad
```

As we all know, the version can be `lateset` or `$ cat VERSION`

## Reference 

Find more information about Miriad at [Miriad](http://www.atnf.csiro.au/computing/software/miriad/)

## travis

[![Build Status](https://www.travis-ci.org/shaoguangleo/AstroSoft.svg?branch=master)](https://www.travis-ci.org/shaoguangleo/AstroSoft)
