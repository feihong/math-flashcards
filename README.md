# Feihong's Math Flashcards

## Installation

- Install [Anki](https://apps.ankiweb.net/)
- Run `make anki`
- Click Sync button and enter your credentials
- Install AnkiConnect extension
  - Go to Tools > Add-ons > Get Add-ons
  - Enter 2055492159 and press OK
  - Restart Anki
  - Visit http://localhost:8765/ to verify that AnkiConnect is running

Install Qalculate! CLI

    brew install libqualculate

Install Julia

    asdf plugin add julia
    asdf install julia latest
    asdf global julia latest

## Commands

Start Anki but using `anki-data` as the data directory

    make anki

Update Anki model templates

    make update

## Links

- [Qalculate! Manual](https://qalculate.github.io/manual/index.html)
