# coding:utf-8

import requests
import json
import base64
import pyttsx3
import pywin32_system32
import time
import yaml


url_online = "https://luka-api.ling.cn/robot-login"
url_nlu_chat = "https://luka-api.ling.cn/nlu/chat"

udid = "FRFFBZYP"
api_version = "v1.14"
Language = "zh_CN"
accept = "application/vnd.luka." + str(api_version) + "+json"
inputfile = "nlutest.txt"

# 获取token
def get_token(url):
    headers = {
        "accept": accept,
        "Content-Type": "application/json",
        "Accept-Language": Language
    }
    data = {
        "data": {
            "type": "robot-login",
            "attributes": {
                "udid": udid
            }
        }
    }
    result = requests.put(url, headers=headers, data=json.dumps(data))
    result = json.loads(result.text)
    token = result["data"]["token"]
    return token

# nlu/chat
def nlu_chat(token, url):
    Authorization = "Bearer" + token
    headers = {
        "accept": accept,
        "Content-Type": "application/json",
        "Accept-Language": Language,
        "Authorization": Authorization
    }
    with open(inputfile, "r") as f:
        for i in f.readlines():
            words = i.strip(" ").strip("\n")
            data = {
                "data": {
                    "type": "nlu", "attributes": {
                        "user_id": "luka_02", "words": words, "machine_sentence": "", "initiative": bool(0), "use_chitchat": 1
                    }
                }
            }
            print("————————————————————————————————————————————")
            print(words)
            engine = pyttsx3.init()
            engine.say("撸卡撸卡")
            engine.say(words)
            engine.runAndWait()
            result = requests.post(url=url, headers=headers, data=json.dumps(data))
            result = json.loads(result.text)   
            script = base64.b64decode(result["data"]["script"]) 
            yamlScript = yaml.load_all(script)
            for i in yamlScript:
                result = i.get("main")
                print(result)
                for j in result:
                    result = j.split(" ")[-1]  
                    print(str(base64.b64decode(result),"utf-8"))
            time.sleep(5)

if __name__ == "__main__":
    nlu_chat(get_token(url_online), url_nlu_chat)
    