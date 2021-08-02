import redis
from src import Redis

class RedisString(Redis):
    def get(self, key):
        """
        Return the value at key ``name``, or None if the key doesn't exist
        """
        return self._redis_client.get(key)
    
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

    def delete(self, *key):
        "Delete one or more keys specified by ``names``"
        return self._redis_client.delete(*key)