SOURCES=tetris.py

.PHONY:all
.ONESHELL: all
all: venv
	. venv/bin/activate
	pip install -r requirements.txt
	autopep8 --in-place --aggressive --aggressive $(SOURCES)
	#mypy --strict --disable-error-code no-redef $(SOURCES)
	python3 $(SOURCES)

venv:
	virtualenv -p python3 venv
