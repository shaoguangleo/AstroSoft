# About

Dockerfile to build a jive5ab image based on Rocky.

## How to run

Just type the following commands

```
# On Linux
$ docker run -it -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix shaoguangleo/rocky-jive5ab

# On MacOSX
# IP=$(ifconfig en1 | grep inet | awk '$1=="inet" {print $2}')
$ docker run -it -e DISPLAY=$IP:0 shaoguangleo/rocky-jive5ab
```

As we all know, the version can be `lateset` or `$ cat VERSION`

## How to compile

Basically, it's very simple to compile using cmake toolchains, but for ancient OS such as Mark6 based on Debian 6 or CMAKE 2.8.2, try using the following command:

```bash
$ cmake -DCMAKE_ASM_COMPILER=/usr/bin/gcc -DCMAKE_ASM_FLAGS=-c jive5ab/src/path
```

## travis

[![Build Status](https://www.travis-ci.org/shaoguangleo/AstroSoft.svg?branch=master)](https://www.travis-ci.org/shaoguangleo/AstroSoft)
