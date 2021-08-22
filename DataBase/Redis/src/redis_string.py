import re
import redis
from src import Redis


class RedisString(Redis):
    def get(self, key):
        """
        Return the value at key ``name``, or None if the key doesn't exist
        """
        return self._redis_client.get(key)

    def get_range(self, key, start, end):
        """
        Returns the substring of the string value stored at ``key``,
        determined by the offsets ``start`` and ``end`` (both are inclusive)
        """
        return self._redis_client.getrange(key, start, end)

    def get_bit(self, name, offset):
        "Returns a boolean indicating the value of ``offset`` in ``name``"
        return self._redis_client.getbit(name, offset)

    def get_set(self, name, value):
        """return old value, set new value

        Args:
            name ([string]): [key name]
            value ([string]): [set value]
        """
        return self._redis_client.getset(name, value)

    def gets(self, keys: list):
        """
        Returns a list of values ordered identically to ``keys``
        """
        return self._redis_client.mget(keys)

    def set(self, key, **kwargs):
        """
        Set the value at key ``name`` to ``value``

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

        ``nx`` if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.

        ``xx`` if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.

        ``keepttl`` if True, retain the time to live associated with the key.
            (Available since Redis 6.0)
        """
        return self._redis_client.set(key, **kwargs)

    def sets(self, mapping: dict):
        """
        Sets key/values based on a mapping. Mapping is a dictionary of
        key/value pairs. Both keys and values should be strings or types that
        can be cast to a string via str().
        """
        return self._redis_client.mset(mapping)
    
    def incr(self, key, amount=1):
        """
        Increments the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as ``amount``
        """
        return self._redis_client.incr(key, amount)

    def decr(self, key, amount=1):
        """
        Decrements the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as 0 - ``amount``
        """
        # An alias for ``decr()``, because it is already implemented
        # as DECRBY redis command.
        return self._redis_client.decr(key, amount)
    
    def delete(self, *key):
        "Delete one or more keys specified by ``names``"
        return self._redis_client.delete(*key)

    def get_len(self, name):
        "Return the number of bytes stored in the value of ``name``"
        return self._redis_client.strlen(name)