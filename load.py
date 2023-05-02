from concurrent.futures import ProcessPoolExecutor
import requests
import sys
url = "http://192.168.1.41:31112/function/cpu-intensive-func"

data = {"input": "value"}
def call_func_by_req(counts):
    # Send 10 requests simultaneously
    responses = []
    for i in range(counts):
        try:
            response = requests.post(url, json=data)
            print("call ",i)
            responses.append(response)
            print("response",i)
        except Exception as e:
            print("send the requests",e)
    # Print the responses
    for response in responses:
        try:
            print(response.text)
        except Exception as e:
            print("response ",e)

def call_func(i):
    print("proc i",i)
    try:
        response = requests.post(url)
        print(response.text)
    except Exception as e:
        print("response ", e)


def call_func_by_pro(counts):
    exc = ProcessPoolExecutor(max_workers=counts)
    for i in range(counts):
        try:
            exc.submit(call_func,i)
        except Exception as e:
            print("send the requests",e)
    exc.shutdown()


def main():
    if len(sys.argv) == 1:
        counts = 2
    else:
        counts = int(sys.argv[1])
    call_func_by_pro(counts)

main()
