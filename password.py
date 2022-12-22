#!/usr/bin/env python3
import argparse
import pyperclip
import secrets
import string


class Password:
    """Random Password Generator"""

    def __init__(self, number, length, special):
        """Init"""
        self.number = number
        self.length = length
        self.special = special
        self.buffer = []
        for i in range(self.number):
            self.buffer.append(self.get_password())

    def get_password(self):
        """Generate a random password"""
        if self.special:
            alphabet = string.ascii_letters + string.digits + string.punctuation
        else:
            alphabet = string.ascii_letters + string.digits
        password = "".join(secrets.choice(alphabet) for i in range(self.length))
        return password

    def get_string(self):
        """Return password buffer as string"""
        return "\n".join(self.buffer)

    def get_buffer(self):
        """Return password buffer"""
        return self.buffer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument(
        "-l", "--length", type=int, help="Length of password", default=35
    )
    parser.add_argument(
        "-n", "--number", type=int, help="Number of passwords", default=1
    )
    parser.add_argument("-c", "--clipboard", action="store_true")
    parser.add_argument("-s", "--special", action="store_true")
    args = parser.parse_args()
    password = Password(args.number, args.length, args.special)
    print(password.get_string())
    if args.clipboard:
        pyperclip.copy(password.get_string())
