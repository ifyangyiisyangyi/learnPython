'''
读配置文件
'''
import yaml
import os

filePath = os.path.dirname(os.path.realpath(__file__))  # 返回.py文件的绝对路径
yamlPath = os.path.join(filePath, "env.yml")  # 路径拼接，返回配置文件的绝对路径
f = open(yamlPath, 'r', encoding='utf-8')
result = f.read()
test_data = yaml.load(result, Loader=yaml.FullLoader) # PyYaml 5.1版本弃用了load()原本用法，需要加上 Loader


if __name__ == '__main__':
    print(test_data)
