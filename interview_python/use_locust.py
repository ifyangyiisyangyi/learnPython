"""
use locust
"""

from locust import HttpLocust, TaskSet

def test_index(l):
    l.client.get('/')

def test_article(l):
    l.client.get('/2019/09/09/generalnewsextractor/')

class UserBehavior(TaskSet):
    tasks = [test_index, test_article]

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host='https://www.kingname.info'
    min_wait = 2000
    max_wait = 3000
