# Para instalar en otros SOs ver:
# - stackoverflow.com/a/21530768/3414720
# - cython.readthedocs.io

.PHONY: build

debian-install:
	apt install python3-dev cython3

build:
	python3 setup.py build_ext --inplace
