from inspect import FrameInfo
import copy

from src import Redis


class RedisList(Redis):
    def __init__(self, key):
        Redis.__init__(self)
        self._key = key

    def lpop(self):
        "Remove and return the first item of the list ``name``"
        return self._redis_client.lpop(self._key)

    def rpop(self):
        "Remove and return the last item of the list ``name``"
        return self._redis_client.rpop(self._key)

    def blpop(self, keys, timeout):
        """
        LPOP a value off of the first non-empty list
        named in the ``keys`` list.

        If none of the lists in ``keys`` has a value to LPOP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.
        """
        return self._redis_client.blpop(keys, timeout)

    def lpush(self, *values):
        "Push ``values`` onto the head of the list ``name``"
        return self._redis_client.lpush(self._key, *values)

    def rpush(self, *values):
        "Push ``values`` onto the tail of the list ``name``"
        return self._redis_client.rpush(self._key, *values)

    def lpushx(self, value):
        "Push ``value`` onto the head of the list ``name`` if ``name`` exists"
        return self._redis_client.lpushx(self._key, value)

    def lindex(self, index):
        """
        Return the item from list ``name`` at position ``index``

        Negative indexes are supported and will return an item at the
        end of the list
        """
        return self._redis_client.lindex(self._key, index)

    def lrange(self, left, right):
        """
        Return a slice of the list ``name`` between
        position ``start`` and ``end``

        ``start`` and ``end`` can be negative numbers just like
        Python slicing notation
        """
        return self._redis_client.lrange(self._key, left, right)

    def __len__(self):
        return self._redis_client.llen(self._key)
    
    def __getitem__(self, key):
        if isinstance(key, int):
            return self.lindex(key)
        if isinstance(key, slice):
            start = key.start
            stop = key.stop
            if start is None:
                start = 0
            
            if stop is None:
                stop = len(self) - 1
            else:
                stop -= 1
                
            return self.lrange(start, stop)
        else:
            raise TypeError