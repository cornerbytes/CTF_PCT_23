import requests

if __name__ == "__main__":
    for i in range(2000):
        requests.get('http://localhost:5000/')
        print(i, end="\r", flush=True)
