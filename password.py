#!/usr/bin/env python3
import secrets
import string
import argparse

parser = argparse.ArgumentParser(description='Password Generator')
parser.add_argument("-l","--length",type=int,help="Length of password",
                        default=35)
args = parser.parse_args()

alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(args.length))
print(password)

