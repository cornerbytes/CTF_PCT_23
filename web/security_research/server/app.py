from flask import Flask, request, jsonify, make_response, render_template
from urllib.parse import urlparse
from subprocess import check_output
from os import getenv
import urllib.request

app = Flask(__name__)
FLAG = getenv('FLAG')

@app.route('/hidden_service', methods=["POST"])
def parse_parse():
    if request.is_json:
        data = request.json 
        list_provider = ["wget", "curl", "python"]

        try:
            if data['provider'] not in list_provider:
                return {"message": "provider not available"}, 400

            if urlparse(data['url']).scheme in ["file", "ftp", "gopher"]:
                return {"message": "scheme invalid"}, 403

            if urlparse(data['url']).hostname in ["127.0.0.1", "localhost"]:
                return {"message": "can't fetch localhost"}, 403

            if data["provider"] == "curl":
                return check_output(["curl", data["url"]]).decode()
            
            if data["provider"] == "wget":
                return check_output(["wget", data["url"], "-O", "-"]).decode()
            
            if data["provider"] == "python":
                return urllib.request.urlopen(data["url"]).read()

        except Exception as e:
            print(e)
            return {"message" : f"unknown error"}, 400
    else:
        return {"message": "please send a json object"}, 400

@app.route('/get_flag', methods=["GET"])
def get_flag():
    if request.remote_addr == "127.0.0.1":
        return {"message": FLAG}
    else:
        return {"message": "unauthorized"}, 401

@app.route('/', methods=["GET"])
def route_root():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=False)
