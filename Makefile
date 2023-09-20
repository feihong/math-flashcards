install:
	pip install --requirement requirements.txt

anki:
	python open_anki.py

publish:
	python publish.py

build:
	python build.py

update: build
	python update_anki.py
