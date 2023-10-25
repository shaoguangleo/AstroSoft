# About

The image is built on top of the most recently `ubuntu` image and installs the following extra packages:

- `mpi4py`
- `requests`
- `numpy`

The packages are selected for common use in the future. 

# How to run

Just type the following commands

```bash
$ docker run -it -p 8888:8888 -v /Users/leo/OneDrive/git_internal/my/SHAO-SKA/HeTu/:/hetu shaoguangleo/hetu
$ cd /hetu
$ . /ai/bin/activate
$ jupter-notebook --allow-root
```

As we all know, the version can be `lateset` or `$ cat VERSION`

# travis

[![Build Status](https://www.travis-ci.org/shaoguangleo/docker-hetu.svg?branch=master)](https://www.travis-ci.org/shaoguangleo/docker-hetu)


# Run HeTu

```bash
# start the docker
$ docker run -it -v /o9000/MWA/GLEAM-X/GLEAM-X-IDR1/HETU-GLEAM-X/code/:/code -v /o9000/MWA/GLEAM/hetu_images/deep_learn/inference_sets/:/catalogue -v /o9000/MWA/GLEAM/hetu_images/deep_learn/inference_sets/FIRST_fits-10G:/output shaoguangleo/hetu

# start the downloading
$ cd code/158
$ bash FIRST_fits_files_all_multnodes_fixed-158-docker.sh
```