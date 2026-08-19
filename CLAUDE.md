# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository overview

This is a personal collection of standalone Python utility scripts built while working through *Automate the Boring Stuff with Python*, plus a couple of unrelated experiments (`kivy/`, `python_fire/`). There is no shared application, package, or entry point — each `.py` file in the repo root is an independent CLI tool with its own `if __name__` / argparse block. Do not assume changes in one script affect another.

## Scripts (repo root)

* `calc.py` — n/a (see `python_fire/calc.py`)
* `check_port.py` — checks whether a TCP port is open (`argparse`, `socket`)
* `cidr.py` — converts a CIDR range to its first/last IP (`ipaddress`, `argparse`)
* `clippy.py` — polls the clipboard and appends new entries to a YAML history file; config comes from `clippy.toml` (keys: `history` path, `size` max entries)
* `downloads.py` — sorts files in the current working directory into subfolders by extension, per the mapping in `mapping.yaml`
* `gitremote.py` — converts a git SSH remote URL into an HTTPS URL and opens it in a browser
* `mapIt.py` — opens a Google Maps search for an address passed as args or read from the clipboard
* `password.py` — random password generator (`secrets`, `string`); exposes a `Password` class as well as a CLI

`searchIt.py` (mentioned in README) has moved to a separate repo: https://github.com/alastairhm/searchit — do not recreate it here.

### Subdirectories

* `python_fire/` — small examples of the [`fire`](https://github.com/google/python-fire) CLI library (`hello.py`, `hello2.py`, `calc.py`). Has its own venv (`python_fire/.env`) and `requirements.txt`.
* `kivy/` — a minimal Kivy app experiment (`test.py`). Its `requirements.txt` is kept current via Dependabot — expect frequent automated version-bump PRs/commits scoped to this folder only.
* `archive/` — currently empty; holding place for retired scripts.

## Running scripts

There is no unified dependency file or build system. Each script/subfolder manages its own dependencies:

```bash
# repo-root scripts share the top-level .env venv
source .env/bin/activate
python3 <script>.py [args]

# clippy.py additionally needs its own requirements
pip install -r clippy_req.txt

# python_fire/ and kivy/ are self-contained
cd python_fire && source .env/bin/activate && pip install -r requirements.txt
cd kivy && pip install -r requirements.txt
```

Most scripts accept `-h`/`--help` via `argparse` for usage details.

## Workflow

* Never commit directly to `main`. Create a feature branch, push it, and open a PR for review/approval — for every change, not just large ones.
* Always keep `CHANGELOG.md` and `README.md` up to date as part of the same change (see conventions below), not as a follow-up.

## Conventions in this codebase

* Scripts are shebanged (`#!/usr/bin/env python3`) and executable; keep that pattern for new scripts.
* Config lives next to the script that uses it (`clippy.toml`, `mapping.yaml`), loaded via `os.path.dirname(os.path.abspath(__file__))` so scripts work regardless of the caller's cwd.
* YAML loads use `yaml.load_all(..., Loader=SafeLoader)` — keep using `SafeLoader`, not the default loader.
* No test suite, linter config, or CI currently exists in this repo — don't assume one and don't add heavyweight tooling unless asked.
* `CHANGELOG.md` follows Keep a Changelog format; update its `Unreleased` section when adding a new script, matching the existing "* Description [alastairhm](https://github.com/alastairhm)" style.
* `README.md`'s Scripts list should stay in sync with the root-level scripts.
