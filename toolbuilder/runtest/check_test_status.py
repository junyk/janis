import sys
import requests

def check_test_status(run_id: str):
    print(run_id)


if __name__ == "__main__":
    check_test_status(sys.argv[1])
