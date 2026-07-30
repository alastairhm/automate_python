#!/usr/bin/env python3
"""Convert CIDR to IP Range"""

import ipaddress
import argparse
import sys

parser = argparse.ArgumentParser(description="CIDR to IP Range")
parser.add_argument("-c", "--cidr", type=str, help="CIDR Range", default="10.0.0.0/8")
args = parser.parse_args()

try:
    net = ipaddress.ip_network(args.cidr)
except ValueError as e:
    sys.exit(f"Invalid CIDR range '{args.cidr}': {e}")

print(net[0], "-", net[-1])
