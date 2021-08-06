#!/usr/bin/env python3

import pyperclip
import time
import datetime

cliptext = ""
while True:
    tmptext = pyperclip.paste()
    if tmptext != cliptext:
        now = datetime.datetime.now()
        cliptext = tmptext
        with open("/Users/alastair.montgomery/gitrp/notes/clip.txt", "r+") as f:
            content = f.read()
            f.seek(0)
            f.write(now.strftime('%Y-%m-%d %H:%M:%S') + " : " +cliptext + "\n" + "----------\n" + content)
    time.sleep(1)

