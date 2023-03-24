
import redis


class RedisHelper():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.r = redis.Redis(host=self.host, port=self.port)

    def set_value(self, key, value):
        self.r.set(key, value)

    def get_value(self, key):
        return self.r.get(key)

    def delete_key(self, key):
        self.r.delete(key)

    def get_all_keys(self):
        return self.r.keys()
