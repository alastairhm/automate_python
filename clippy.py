#!/usr/bin/env python3

import pyperclip
import time
import yaml
import toml
import os
from yaml.loader import SafeLoader

script_path = os.path.dirname(os.path.abspath(__file__))
settings = toml.load(os.path.join(script_path, "clippy.toml"))
history = settings["history"]
max_size = settings["size"]

cliptext = ""
clip_array = []
with open(history, "r") as f:
    clip_array = list(yaml.load_all(f, Loader=SafeLoader))
    clip_array = sum(clip_array, [])

while True:
    tmptext = pyperclip.paste()
    if tmptext != cliptext:
        cliptext = tmptext
        if cliptext not in clip_array:
            clip_array.insert(0, tmptext)
            if len(clip_array) > max_size:
                clip_array.pop()
            with open(history, "w") as f:
                f.write(yaml.dump(clip_array))
    time.sleep(1)
