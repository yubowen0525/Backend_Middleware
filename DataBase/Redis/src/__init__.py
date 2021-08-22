import redis
from redis.client import Redis
connector_string = "redis://:@localhost:6379/0"

def get_redis():
    return redis.from_url(connector_string, decode_responses=True) 
    

class Redis(object):
    def __init__(self):
        self._redis_client = None
        self.init()
        
    def init(self):
        self._redis_client =  get_redis()
    
    
    