install:
	pip install --requirement requirements.txt

anki:
	open -a Anki --args -b ~/anki-data

publish:
	python publish.py

build:
	python build.py

update: build
	python update_anki.py
