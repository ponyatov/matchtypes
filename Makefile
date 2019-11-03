MODULE = $(notdir $(CURDIR))

go: bin/python $(MODULE).py
	./$^

install:
	pip install -U pip
	pip install -U -r requirements.txt
	$(MAKE) requirements.txt
.PHONY: requirements.txt
requirements.txt:
	pip freeze | grep -v 0.0.0 > $@

