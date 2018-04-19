VERSION := $(shell python setup.py --version)
NAME := $(shell python setup.py --name)
NAME_NORMALIZED := $(shell echo ${NAME} | sed s/-/_/)

help:
	@echo "make sdist           - Creates python source packages"
	@echo "make pypi            - Updates PyPI package"
	@echo "make requirements    - Updates requirements files"
	@echo "make test            - Runs tests"
	@echo "make clean           - Gets rid of scratch and byte files"

sdist:
	python setup.py sdist --formats=gztar

wheel:
	python setup.py bdist_wheel

dist: sdist wheel

sign_wheel:
	wheel sign dist/${NAME_NORMALIZED}-${VERSION}-*.whl

sign:
	wheel verify dist/${NAME_NORMALIZED}-${VERSION}-*.whl
	sh -c 'read -s -p "Enter GPG passphrase: " pwd && \
	gpg --detach-sign --batch --yes --armor --passphrase $$pwd dist/${NAME}-${VERSION}.tar.gz && \
	gpg --detach-sign --batch --yes --armor --passphrase $$pwd dist/${NAME_NORMALIZED}-${VERSION}-*.whl'
	@echo

pypi: dist sign
	twine upload dist/{${NAME},${NAME_NORMALIZED}}-${VERSION}*

requirements:
	# it's a hack for installing modules from a git repository
	pip freeze|sed -e 's%\(.*/[a-z]*\.git\)@[0-9a-f]*\(#.*\)%\1\2%' > requirements.txt

test:
	python setup.py test

clean:
	python setup.py clean
	rm -fr build/ dist/ .eggs/ .tox/
	rm -fr *.egg-info/
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
