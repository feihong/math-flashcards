install:
	pip install --requirement requirements.txt

build:
	python build.py

publish: build
	python publish.py

serve: build
	cd content && python -m http.server

update: build
	python update_anki.py
