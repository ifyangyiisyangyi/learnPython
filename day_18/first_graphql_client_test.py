
from graphqlclient import GraphQLClient

client = GraphQLClient('http://luka-graphql.zhangfeifei.linglove.cn/graphql')
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
    "name": "18510086742",
    "password": "12345678"
}


result = client.execute(query=query, variables=variables)

print(result)