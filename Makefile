install:
	pip install --requirement requirements.txt

publish:
	python publish.py

build:
	python build.py

update: build
	python update_anki.py
