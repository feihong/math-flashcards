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

Install Go

    asdf plugin add golang
    asdf install golang latest
    asdf global golang latest

Install ivy

    go install robpike.io/ivy@latest
    echo alias ivy=\"rlwrap $(go env GOPATH)/bin/ivy\"

Add the result of the last command to your `~/.zprofile`.

## Commands

Start Anki but using `anki-data` as the data directory

    make anki

Update Anki model templates

    make update

## Links

- [Qalculate! Manual](https://qalculate.github.io/manual/index.html)
- [Ivy docs](https://pkg.go.dev/robpike.io/ivy)
