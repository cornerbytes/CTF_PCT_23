import requests
import json

if __name__ == "__main__":
    url = "http://127.0.0.1:5000/hidden_service"
    payload = {
        "provider": "curl",
        "url" : "http://supercalifragilisticexpialidocious.co.uk:5000/"
    }
    headers = {'Content-Type': "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code, response.text)
