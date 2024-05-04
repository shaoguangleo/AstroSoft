OS=ubuntu-miriad

all: build release

build:
	@docker build --tag=shaoguangleo/$(OS):latest .

release: build
	@docker build --tag=shaoguangleo/$(OS):$(shell cat VERSION) .

push:
	@docker push shaoguangleo/$(OS):$(shell cat VERSION)
	@docker push shaoguangleo/$(OS):latest

output:
	@docker save --output=${shell pwd}/$(OS):$(shell cat VERSION).tar shaoguangleo/$(OS):$(shell cat VERSION)

input:
	@docker load --input=${shell pwd}/$(OS):$(shell cat VERSION).tar
