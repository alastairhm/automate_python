#!/usr/bin/env python3

import os
import sys

directory = os.getcwd()
print(directory)


file_folder_mapping = {
    '.csv':'data',
    '.dmg':'bundles',
    '.docx':'documents',
    '.gif':'images',
    '.gz':'bundles',
    '.iso':'iso',
    '.jpeg':'images',
    '.jpg':'images',
    '.json':'data',
    '.mkv':'videos',
    '.mp3':'audio',
    '.mp4':'videos',
    '.pdf':'pdfs',
    '.png':'images',
    '.txt':'documents',
    '.xlsx':'data',
    '.xml':'data',
    '.yaml':'data',
    '.zip':'bundles',
}

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        ext = os.path.splitext(f)
        if ext[1] != '':
            print(os.path.basename(f))
            sub_directory = file_folder_mapping.get(ext[1].lower(),"misc")
            if not os.path.exists(sub_directory):
                os.makedirs(sub_directory)
            os.rename(f,os.path.join(sub_directory,f))