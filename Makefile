help:
	@echo "make requirements    - Updates requirements files"

requirements:
	# it's a hack for installing modules from a git repository
	pip freeze|sed -e 's%\(.*/[a-z]*\.git\)@[0-9a-f]*\(#.*\)%\1\2%' > requirements.txt
