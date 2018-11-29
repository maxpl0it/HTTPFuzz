![Alt text](/images/httpfuzz.png)

## Introduction

> HTTPFuzzer can be used to generate vast amounts of both valid and invalid HTTP requests, allowing you to test both web application and web server handling of requests.

## Running HTTPFuzz

Generate a random request:
```
python httpfuzz.py
```

Generate a valid request:
```
python httpfuzz.py --header-mutate-level=0 --body-mutate-level=0 --request-mutate-level=0
```

Generate a request with a json body:
```
python httpfuzz.py --body-mutate-level=0 --body-type=json
```

Full help:
```
usage: httpfuzz.py [-h] [--header-mutate-level [{0,1,2,3,4,5,6,7,8,9,10}]]
                   [--body-mutate-level [{0,1,2,3,4,5,6,7,8,9,10}]]
                   [--request-mutate-level [{0,1,2,3,4,5,6,7,8,9,10}]]
                   [--body-type {json,junk,rand}] [--num-headers NUM_HEADERS]
                   [--generate-num GENERATE_NUM] [-v]

optional arguments:
  -h, --help            show this help message and exit
  --header-mutate-level [{0,1,2,3,4,5,6,7,8,9,10}]
                        Set the mutation level for the headers (0-10). Default
                        = 5
  --body-mutate-level [{0,1,2,3,4,5,6,7,8,9,10}]
                        Set the mutation level for the body (0-10). Default =
                        5
  --request-mutate-level [{0,1,2,3,4,5,6,7,8,9,10}]
                        Set the mutation level for the request line (0-10).
                        Default = 5
  --body-type {json,junk,rand}
                        Set the data generated in the request body. Default =
                        rand
  --num-headers NUM_HEADERS
                        Sets the maximum number of headers. Default = number
                        of available headers
  --generate-num GENERATE_NUM
                        Number of requests to generate. Any more than 1
                        generated request will output to a new folder called
                        output/. Default = 1
  -v, --version         show program's version number and exit
```
