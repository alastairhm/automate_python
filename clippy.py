#!/usr/bin/env python3

import pyperclip
import time
import yaml
from yaml.loader import SafeLoader

cliptext = ""
clip_array = []
with open("/Users/alastair.montgomery/gitrp/notes/clip.yml", "r") as f:
    clip_array = list(yaml.load_all(f, Loader=SafeLoader))
    clip_array = sum(clip_array, [])

while True:
    tmptext = pyperclip.paste()
    if tmptext != cliptext:
        cliptext = tmptext
        if cliptext not in clip_array:
            clip_array.insert(0,tmptext)
            if len(clip_array) > 100:
                clip_array.pop()
            with open("/Users/alastair.montgomery/gitrp/notes/clip.yml", "w") as f:
                f.write(yaml.dump(clip_array))
    time.sleep(1)
