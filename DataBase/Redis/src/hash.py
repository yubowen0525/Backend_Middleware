import re
import redis
from src import Redis


class RedisHash(Redis):
    def __init__(self, key):
        Redis.__init__(self)
        self._key = key

    def hincrby(self, key, amount=1):
        "Increment the value of ``key`` in hash ``name`` by ``amount``"
        return self._redis_client.hincrby(self._key, key, amount)

    def hincrbyfloat(self, key, amount=1.0):
        "Increment the value of ``key`` in hash ``name`` by ``amount``"
        return self._redis_client.hincrbyfloat(self._key, key, amount)

    def hget(self, key):
        "Return the value of ``key`` within the hash ``name``"
        return self._redis_client.hget(self._key, key)

    def hmget(self, keys, *args):
        "Returns a list of values ordered identically to ``keys``"
        return self._redis_client.hmget(self._key, keys, *args)
    
    def hscan(self,cursor=0, match=None, count=None):
        """
        Incrementally return key/value slices in a hash. Also return a cursor
        indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns
        """
        return self._redis_client.hscan(self._key,cursor, match, count)

    def hkeys(self):
        "Return the list of keys within hash ``name``"
        return self._redis_client.hkeys(self._key)
    
    def hvals(self):
        "Return the list of values within hash ``name``"
        return self._redis_client.hvals(self._key)

    def hlen(self):
        "Return the number of elements in hash ``name``"
        return self._redis_client.hlen(self._key)

    def hgetall(self):
        "Return a Python dict of the hash's name/value pairs"
        return self._redis_client.hgetall(self._key)

    def hset(self, key=None, value=None, mapping=None):
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that that will be
        added to hash ``name``.
        Returns the number of fields that were added.
        """
        return self._redis_client.hset(self._key, key, value, mapping)

    def hmset(self, mapping):
        """
        Set key to value within hash ``name`` for each corresponding
        key and value from the ``mapping`` dict.
        """
        return self._redis_client.hmset(self._key, mapping)

    def hdel(self, *key):
        "Delete ``keys`` from hash ``name``"
        return self._redis_client.hdel(self._key, *key)

    def hexist(self, key):
        "Returns a boolean indicating if ``key`` exists within hash ``name``"
        return self._redis_client.hexists(self._key, key)

    def __len__(self):
        return self.hlen()
