#!/usr/bin/env python3

import argparse

# sys.argv
# -h
# --port 7777

parser = argparse.ArgumentParser()

parser.add_argument("--host", type = str, default = "127.0.0.1", help = "host ip address")
parser.add_argument("--port", type = int, default = 7777, help = "host port")

args = parser.parse_args()

print(args.host, args.port)

