"""
learn redis
"""

import redis
r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
r.set('test', 'yy')
print(r.get('test'))
