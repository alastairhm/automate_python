#!/usr/bin/env python3
'''Quick searching from command line'''

import webbrowser
import sys
import os
import pyperclip
import toml

script_path = os.path.dirname(os.path.abspath(__file__))
settings = toml.load(os.path.join(script_path, "searchIt.toml"))
engine = settings["default"]
search_url = settings[engine]

if len(sys.argv) > 1:
    search_term = " ".join(sys.argv[1:])
else:
    search_term = pyperclip.paste()

webbrowser.open(search_url + search_term)
