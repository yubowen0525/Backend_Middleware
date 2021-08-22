from inspect import FrameInfo
import re


from src import Redis


class RedisSet(Redis):
    def __init__(self, key):
        Redis.__init__(self)
        self._key = key

    def sadd(self, *key):
        "Add ``value(s)`` to set ``name``"
        return self._redis_client.sadd(self._key, *key)

    def scard(self):
        "Return the number of elements in set ``name``"
        return self._redis_client.scard(self._key)

    def sdiff(self, keys: list, *args):
        "差集  Return the difference of sets specified by ``keys``"
        keys.append(self._key)
        return self._redis_client.sdiff(keys, *args)

    def sdiffstore(self, dest, keys: list, *args):
        """
        Store the difference of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.
        """
        keys.append(self._key)
        return self._redis_client.sdiffstore(dest, keys, *args)

    def sinter(self, keys: list, *args):
        "交集  Return the intersection of sets specified by ``keys``"
        keys.append(self._key)
        return self._redis_client.sinter(keys, *args)

    def sunion(self, keys: list, *args):
        "并集  Return the union of sets specified by ``keys``"
        keys.append(self._key)
        return self._redis_client.sunion(keys, *args)
    
    def smember(self):
        "Return all members of the set ``name``"
        return self._redis_client.smembers(self._key)

    def sismember(self, key):
        "Return a boolean indicating if ``value`` is a member of set ``name``"
        return self._redis_client.sismember(self._key, key)

    def smove(self, dst, key):
        "Move ``value`` from set ``src`` to set ``dst`` atomically"
        return self._redis_client.smove(self._key, dst, key)
    
    def srem(self, *key):
        "Remove ``values`` from set ``name``"
        return self._redis_client.srem(self._key, *key)