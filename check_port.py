#!/usr/bin/env python

'''Check Port is Open'''

import socket
import argparse

def check_port(address, port):
    '''Check Port is open'''

    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    location = (address, port)
    check = a_socket.connect_ex(location)

    if check == 0:
        print("Port is open")
    else:
        print("Port is not open")


parser = argparse.ArgumentParser(description='Port Checker')
parser.add_argument("-a","--address",type=str,help="Address", default="localhost")
parser.add_argument("-p","--port",type=int,help="Port Number", default=8080)
args = parser.parse_args()

check_port(args.address, args.port)
