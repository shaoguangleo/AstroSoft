# AstroSoft 

[![DOI](https://zenodo.org/badge/40939159.svg)](https://zenodo.org/doi/10.5281/zenodo.11219200)

```
    _      ____     ___    ____
   / \    / ___|   / _ \  |  _ \
  / _ \   \___ \  | | | | | | | |
 / ___ \   ___) | | |_| | | |_| |
/_/   \_\ |____/   \___/  |____/

```

ASOD is the abbreviation of **A**stro**S**oft **O**n **D**ocker.

Any problem , send email to me [郭大侠](https://github.com/shaoguangleo) <sgguo@shao.ac.cn> @ [上海天文台](http://www.shao.ac.cn)

# Introduction

This git repo will hold all the related astrosoft dockers and **sas** (*S*HAO *A*stronomical *S*oftware)。

致力于精简所有天文流行软件的安装，只需一条命令即可使用复杂的可能要花上几天来安装的软件。

上一个版本主要基于源码安装，操作有些复杂，详细的脚本可以参考old目录。

最新版本基于Docker，只需`docker run`即可享用相应软件。

另外增加sas软件安装包，使用详情见如何使用sas章节。

# DOCKER

## Support OS and Software

All the docker images can run on the following OS:

- Ubuntu
- CentOS
- MacOSX
- Other Linux Distro is support

## 使用方法



使用方法很简单，只要下面一个命令即可：

```
$ docker run -it docker_name[:version]
```

其中*docker_name*为下面章节中的名字，比如如果希望之使用centos的pgplot版本，输入下述命令即可：

```
$ docker run -it shaoguangleo/centos-pgplot
```

另外*version*为版本号，除非特别说明，默认拉取*latest*最新版本。


## Docker 情况

目前支持的软件，如下所示：

|     | Ubuntu     |  CentOS    |  版本 |
|----|-----|-----|-----|
|basic|:+1:shaoguangleo/ubuntu| :+1:shaoguangleo/centos | CentOS:7.4 </br> Ubuntu:17.10|
|pgplot|:+1:shaoguangleo/ubuntu-pgplot| :+1:shaoguangleo/centos-pgplot | PGPLOT : v5.2.2 |
|tempo|:+1:[shaoguangleo/ubuntu-tempo](https://github.com/shaoguangleo/docker-ubuntu-tempo) |:+1:[shaoguangleo/centos-tempo](https://github.com/shaoguangleo/docker-centos-tempo)|Tempo V20170729 |
|tempo2|:construction:​|:construction:​||
|sigproc|:construction:​|:construction:​||
|presto|:+1:[shaoguangleo/ubuntu-presto](https://github.com/shaoguangleo/docker-ubuntu-presto)|:+1:shaoguangleo/centos-presto|Presto v2.1|
|psrcat|:construction:​|:construction:​||
|cfitsio|:construction:​|:construction:​||
|calceph|:construction:​|:construction:​||
|psrchive|:construction:​|:construction:​||
|dspsr|:construction:​|:construction:​||
|DiFX|:construction:​|:+1: shaoguangleo/centos-difx| DiFX v2.5.1/v2.5.2 |
|SFXC|:construction:​|:construction:​||
|Difmap|:construction:​|:construction:​||
|sd| :+1:[shaoguangleo/ubuntu-sd](https://github.com/shaoguangleo/docker-ubuntu-sd/) |:construction:| sd : v0.1 |
|fs|:construction:|:+1: shaoguangleo/centos-fs| FS-10.1.1 |
|wsclean|:construction:|:+1: shaoguangleo/centos-wsclean| wsclean 3.2 |


## Current relationship

![wait](images/astrosoft_relationship.png)

# SAS

## How to install sas

Just enter the src directory and type `make install`, you will have all the program you need.

## How to install astronomical software

This is a collection program writen by python/bash inspre by psrsoft, I just want to make this like yum or apt. What you need to do is

```
$ sas software
```

If you just type `sas`, you will get a help information of how to use sas like the following information.

# 软件版本

目前大部分版本因为托管在git上，更新比较快，除了稳定发布的tag版本，其他按照提交时间来发布。

下属命令可以获取最新提交时间信息。

```bash
$ git show -s --pretty=format:%cI
```

## Maintainer

- [@shaoguangleo](https://github.com/shaoguangleo)
- [@Xu-Zhijun](https://github.com/Xu-Zhijun)