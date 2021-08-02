import redis
from redis.client import Redis
connector_string = "redis://:@localhost:6379/0"

redis_client = redis.from_url(connector_string)

class Redis(object):
    def __init__(self):
        self._redis_client = None
        
    def init(self):
        return redis.from_url(connector_string)
    
    
    