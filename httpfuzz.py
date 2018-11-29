# Testing
import sys, os
sys.dont_write_bytecode = True

import argparse, socket
from requestframe import RequestFrame

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--header-mutate-level", type=int, choices=range(11), nargs='?', help="Set the mutation level for the headers (0-10). Default = 5", default=5)
    parser.add_argument("--body-mutate-level", type=int, choices=range(11), nargs='?', help="Set the mutation level for the body (0-10). Default = 5", default=5)
    parser.add_argument("--request-mutate-level", type=int, choices=range(11), nargs='?', help="Set the mutation level for the request line (0-10). Default = 5", default=5)
    parser.add_argument("--body-type", type=str, choices=['json', 'junk', 'rand'], help="Set the data generated in the request body. Default = rand", default='rand')
    parser.add_argument("--num-headers", type=int, help="Sets the maximum number of headers. Default = number of available headers", default=-1)
    parser.add_argument("--generate-num", type=int, help="Number of requests to generate. Any more than 1 generated request will output to a new folder called output/. Default = 1", default=1)
    parser.add_argument('-v', '--version', action='version', version='HTTPFuzz Version: 1.0.1')
    args = parser.parse_args()
    if args.generate_num > 1:
        try:
            os.mkdir("output")
            for i in range(args.generate_num):
                with open("output/{}.txt".format(i + 1), 'w') as f:
                    request_frame = RequestFrame(args)
                    request_frame.generate()
                    f.write(request_frame.request)
                    print("[+] Wrote request to /output/{}.txt".format(i + 1))
            exit("[+] Finished creating requests")
        except:
            exit("[-] Couldn't make the output directory. It might already exist.")
    request_frame = RequestFrame(args)
    request_frame.generate()
    exit(request_frame.request)
