"""
flask test

"""

from flask import Flask, url_for

app = Flask(__name__)

url = "http://luka-api.test1.k8s-qa.linglove.cn"


@app.route('/name/password')
def get_app_token(url):
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
                "name": name,
                "password": password
            }
        }
    }
    result = requests.put(urll, headers=headers, data=json.dumps(data))
    result = json.loads(result.text)
    token = result["data"]["token"]
    return token


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True)
