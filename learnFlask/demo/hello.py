"""
flask test

"""

from flask import Flask, request
from flask import render_template
import requests
import json

app = Flask(__name__)

url = "http://luka-api.test1.k8s-qa.linglove.cn"


# 登录
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
    res = json.dumps(result)
    return res


# html模板
@app.route('/html/')
def test():
    url_str = 'www.yy.com'
    my_list = [1, 2, 3]
    my_dict = {'name': 'yy', 'age': 30}
    return render_template('hello.html', url_str=url_str, my_list=my_list, my_dict=my_dict)


# js模板
@app.route('/')
def js():
    return render_template('index.html')


# 请求对象
@app.route('/method/', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'success'
    else:
        return 'fail'


# 请求传参
@app.route('/orders/<int:order_id>')
def get_order(order_id):
    return f'order id is {order_id}'


'''
目的：实现一个简单的登录逻辑处理
1. 路由实现get,post两种请求方式 --> 需要判断请求参数
2. 获取请求的参数
3. 判断参数是否填写
4. 如果判断没问题，就返回success
'''


# 登录表单
@app.route('/index/', methods=['GET', 'POST'])
def index():
    # 1. 判断请求方式
    if request.method == 'POST':
        # 2. 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        print(type(username))
        print(f'password:{password}')
        # 3. 判断参数是否填写
        if username == '' or password == '':
            print('参数不完整')
        else:
            return 'success'

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)



# 测试git