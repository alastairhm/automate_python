#!/usr/bin/env python3
'''Convert ssh git url into https'''

import argparse
import webbrowser

parser = argparse.ArgumentParser(description='ssh to https')
parser.add_argument("-a","--address",type=str,help='Git Remote URL')
args = parser.parse_args()

raw_url = args.address
if raw_url.startswith("git"):
    url = args.address.split("@")[1].replace(":","/")
else:
    url = raw_url
webbrowser.open(url)
