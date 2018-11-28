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
