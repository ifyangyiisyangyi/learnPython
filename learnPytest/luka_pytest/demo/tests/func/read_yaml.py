'''
日期：2019年4月29日15:06:35

读取配置文件，返回dict
'''
import yaml
import os

filePath = os.path.dirname(os.path.realpath(__file__)) # 返回.py文件的绝对路径
yamlPath = os.path.join(filePath, "yy_data.yaml")  # 路径拼接，返回配置文件的绝对路径
f = open(yamlPath, 'r', encoding = 'utf-8') 
result = f.read()
test_data = yaml.load(result)
print(type(test_data))
print(test_data)