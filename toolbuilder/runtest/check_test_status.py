import sys
import time
import json


def check_test_status(url: str):
    import requests

    status = None
    keep_checking = True
    max_try = 3
    count = 0
    while keep_checking:
        count += 1
        resp = requests.get(url)
        if resp.status_code == requests.codes.ok:
            as_json = resp.json()
            print(as_json)
            if as_json["data"]["status"] in ["failed", "succeeded"]:
                status = as_json["data"]["status"]
                keep_checking = False

        if count >= max_try:
            keep_checking = False

        time.sleep(10)

    if status is None:
        raise Exception("Failed to fetch test status")

    if status != "succeeded":
        raise Exception("Test failed")


if __name__ == "__main__":
    check_test_status(sys.argv[1])
