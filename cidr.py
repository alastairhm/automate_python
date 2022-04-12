#!/usr/bin/env python3
import ipaddress
import argparse

parser = argparse.ArgumentParser(description='CIDR to IP Range')
parser.add_argument("-c","--cidr",type=str,help='CIDR Range',
                        default='10.0.0.0/8')
args = parser.parse_args()

net = ipaddress.ip_network(args.cidr)
print(net[0],'-',net[-1])
