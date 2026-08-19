# automate_python

## Description

Scripts created from [AUTOMATE THE BORING STUFF WITH PYTHON](https://automatetheboringstuff.com/)

## Scripts

* **check_port.py** - checks whether a TCP port on a given address is open
* **cidr.py** - converts a CIDR range into its first and last IP address
* **clippy.py** - polls the clipboard and appends new entries to a YAML history file (config in `clippy.toml`)
* **downloads.py** - sorts files in the current working directory into subfolders by extension, per the mapping in `mapping.yaml`
* **gitremote.py** - converts a git SSH remote URL into an HTTPS URL and opens it in a browser
* **mapIt.py** - opens a Google Maps search for an address passed as args or read from the clipboard
* **password.py** - random password generator (`secrets`, `string`); usable as a CLI or as a `Password` class

`searchIt.py` has moved to its own repo: [https://github.com/alastairhm/searchit](https://github.com/alastairhm/searchit)

## Subdirectories

* **python_fire/** - examples of the [`fire`](https://github.com/google/python-fire) CLI library (`hello.py`, `hello2.py`, `calc.py`)
* **kivy/** - a minimal [Kivy](https://kivy.org/) app experiment (`test.py`)
* **archive/** - holding place for retired scripts (currently empty)
