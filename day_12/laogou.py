# -*- coding: utf-8 -*-
import requests

r = requests.get("http://www.github.com")
# print(r.status_code)
# print(r.json)
# print(r.headers)
# print("-----------")
# print(r.headers['content-type'])
print(r.url)