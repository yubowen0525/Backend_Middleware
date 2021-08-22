from inspect import FrameInfo
import re


from src import Redis


class RedisSortedSet(Redis):
    def __init__(self, key):
        Redis.__init__(self)
        self._key = key

    def zadd(self, mapping, nx=False, xx=False, ch=False, incr=False):
        """
        Set any number of element-name, score pairs to the key ``name``. Pairs
        are specified as a dict of element-names keys to score values.

        ``nx`` forces ZADD to only create new elements and not to update
        scores for elements that already exist.

        ``xx`` forces ZADD to only update scores of elements that already
        exist. New elements will not be added.

        ``ch`` modifies the return value to be the numbers of elements changed.
        Changed elements include new elements that were added and elements
        whose scores changed.

        ``incr`` modifies ZADD to behave like ZINCRBY. In this mode only a
        single element/score pair can be specified and the score is the amount
        the existing score will be incremented by. When using this mode the
        return value of ZADD will be the new score of the element.

        The return value of ZADD varies based on the mode specified. With no
        options, ZADD returns the number of new elements added to the sorted
        set.
        """
        return self._redis_client.zadd(self._key, mapping, nx, xx, ch, incr)

    def zcard(self):
        "Return the number of elements in set ``name``"
        return self._redis_client.zcard(self._key)

    def zcount(self, min, max):
        """
        Returns the number of elements in the sorted set at key ``name`` with
        a score between ``min`` and ``max``.
        """
        return self._redis_client.zcount(self._key, min, max)

    def zincrby(self, amount, value):
        "Increment the score of ``value`` in sorted set ``name`` by ``amount``"
        return self._redis_client.zincrby(self._key, amount, value)

    def zlexconut(self, min, max):
        """
        Return the number of items in the sorted set ``name`` between the
        lexicographical range ``min`` and ``max``.
        """
        return self._redis_client.zlexcount(self._key, min, max)

    def zrange(self, start, end, desc=False, withscores=False, score_cast_func=float):
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results descendingly

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value
        """
        return self._redis_client.zrange(self._key, start, end, desc, withscores, score_cast_func)

    def zrangebylex(self, min, max, start=None, num=None):
        """
        Return the lexicographical range of values from sorted set ``name``
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice of the
        range.
        
        不要在分数不一致的SortSet集合中去使用 ZRANGEBYLEX 指令,因为获取的结果并不准确。
        """
        return self._redis_client.zrangebylex(self._key, min, max, start, num)
    
    def zrangebyscore(self, min, max, start=None, num=None,
                      withscores=False, score_cast_func=float):
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        `score_cast_func`` a callable used to cast the score return value
        """
        return self._redis_client.zrangebyscore(self._key, min, max, start, num, withscores, score_cast_func)
    
    def zrem(self, *key):
        "Remove ``values`` from set ``name``"
        return self._redis_client.zrem(self._key, *key)