# Testing
import sys, os
sys.dont_write_bytecode = True

import argparse, socket
from requestframe import RequestFrame

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--header-mutate-level", type=int, choices=range(10), nargs='?', help="Set the mutation level for the headers (0-10). Default = 5", default=5)
    parser.add_argument("--body-mutate-level", type=int, choices=range(10), nargs='?', help="Set the mutation level for the body (0-10). Default = 5", default=5)
    parser.add_argument("--request-mutate-level", type=int, choices=range(10), nargs='?', help="Set the mutation level for the request line (0-10). Default = 5", default=5)
    parser.add_argument("--body-type", type=str, choices=['json', 'junk', 'rand'], help="Set the data generated in the request body. Default = rand", default='rand')
    args = parser.parse_args()
    request_frame = RequestFrame(args)
    request_frame.generate()
    exit(request_frame.request)
