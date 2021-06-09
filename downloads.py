#!/usr/bin/env python3
"""
Manage download folder
"""

import os
import yaml

from yaml.loader import SafeLoader

directory = os.getcwd()
script_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(script_path, 'mapping.yaml'), 'r') as f:
    mapping_data = list(yaml.load_all(f, Loader=SafeLoader))

file_folder_mapping = mapping_data[0]

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        ext = os.path.splitext(f)
        if ext[1] != '':
            print(os.path.basename(f))
            sub_directory = file_folder_mapping.get(ext[1].lower(), "misc")
            if not os.path.exists(sub_directory):
                os.makedirs(sub_directory)
            os.rename(f, os.path.join(sub_directory, f))
