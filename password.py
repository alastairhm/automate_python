#!/usr/bin/env python3
import argparse
import pyperclip
import secrets
import string


def get_password(length, special):
    if special:
        alphabet = string.ascii_letters + string.digits + string.punctuation
    else:
        alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for i in range(length))
    return password


parser = argparse.ArgumentParser(description="Password Generator")
parser.add_argument("-l", "--length", type=int, help="Length of password", default=35)
parser.add_argument("-n", "--number", type=int, help="Number of passwords", default=1)
parser.add_argument("-c", "--clipboard", action="store_true")
parser.add_argument("-s", "--special", action="store_true")
args = parser.parse_args()

for i in range(args.number):
    pword = get_password(args.length, args.special)
    print(pword)
    if args.clipboard:
        pyperclip.copy(pword)
