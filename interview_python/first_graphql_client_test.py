'''
python请求graphql登录接口，返回token
'''
import json
from graphqlclient import GraphQLClient


def getToken():
  client = GraphQLClient(
      'http://luka-graphql.test1.k8s-qa.linglove.cn/graphql')
  query = """
  mutation signIn($region: Region!, $name: String!, $password: String!){
    signIn(region: $region, name: $name, password: $password){
      token
      tokenType
    }
  }
  """
  variables = {
      "region": "CN",
      "name": "18859285396",
      "password": "123456a"
  }
  result = client.execute(query=query, variables=variables)
  token = json.loads(result)['data']['signIn']['token']
  return token


# 测试
print(getToken())
