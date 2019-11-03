MODULE = $(notdir $(CURDIR))

go: bin/python $(MODULE).py
	./$^

install:
	pip install -U pip
	pip install -U ply
	# pip install -U git+https://github.com/Koziev/rulemma
	pip install -U pymorphy2 pymorphy2-dicts-ru
	pip install -U -r requirements.txt
	$(MAKE) requirements.txt
.PHONY: requirements.txt
requirements.txt:
	pip freeze | grep -v 0.0.0 > $@

