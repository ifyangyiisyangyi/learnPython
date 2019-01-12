import yaml
import os

filePath = os.path.dirname(os.path.abspath(__file__)) # 返回的是 .py 文件的绝对路径
print(__file__)
yamlPath = os.path.join(filePath, 'config.yaml') # 路径拼接
print(yamlPath)

f = open(yamlPath, 'r', encoding = 'utf-8')
y = f.read()
x = yaml.load(y)
print(y)
print(x)
print(type(x))
print(x['info']['name'])
print(type(x['email']['xx']))

print(x.get('email').get('xx'))