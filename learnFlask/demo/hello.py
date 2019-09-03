"""
flask test

"""

from flask import Flask, url_for
from flask import render_template
import requests
import json

app = Flask(__name__)

url = "http://luka-api.test1.k8s-qa.linglove.cn"


@app.route('/login/')
def get_app_token():
    urll = url + "/app-login"
    headers = {
        "Accept": "application/vnd.luka.v1.15+json",
        "Content-Type": "application/json",
        "Accept-Language": "zh_CN"
    }
    data = {
        "data": {
            "type": "app-login",
            "attributes": {
                "region": "CN",
                "name": '18859285396',
                "password": '123456a'
            }
        }
    }
    result = requests.put(urll, headers=headers, data=json.dumps(data))
    result = json.loads(result.text)
    token = result["data"]["token"]
    return token


@app.route('/html/')
def test():
    return render_template('hello.html')


@app.route('/')
def js():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
