MODULE = $(notdir $(CURDIR))

go: bin/python $(MODULE).py
	./$^
