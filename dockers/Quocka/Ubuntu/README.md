# About

Dockerfile to build a Quocka image based on Miriad.

## How to run

Just type the following commands

```
$ docker run -it -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix shaoguangleo/ubuntu-quocka
#or MacOSX

$docker run -it -e DISPLAY=host.docker.internal:0 shaoguangleo/ubuntu-quocka
```

As we all know, the version can be `lateset` or `$ cat VERSION`

## Reference

- See https://github.com/QUOCKA-team/quocka for more details.

## travis

[![Build Status](https://www.travis-ci.org/shaoguangleo/AstroSoft.svg?branch=master)](https://www.travis-ci.org/shaoguangleo/AstroSoft)
