'''
读配置文件
'''
import yaml
import os
import json

filePath = os.path.dirname(os.path.realpath(__file__))  # 返回.py文件的绝对路径
yamlPath = os.path.join(filePath, "env.yml")  # 路径拼接，返回配置文件的绝对路径
envPath = os.path.join(filePath, 'current_env.json')
with open(yamlPath, 'r', encoding='utf-8') as f:
    result = f.read()
    test_data = yaml.load(result, Loader=yaml.FullLoader)  # PyYaml 5.1版本弃用了load()原本用法，需要加上 Loader
if os.path.exists(envPath):
    with open(envPath, 'r', encoding='utf-8') as f:
        result = f.read()
        result = json.loads(result)
    for key in result:
        test_data[key] = result[key]

if __name__ == '__main__':
    print(test_data)
