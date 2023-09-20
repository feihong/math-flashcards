install:
	pip install --requirement requirements.txt

anki:
	python open_anki.py

build:
	python build.py

publish:
	python publish.py
