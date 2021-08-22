import pytest
from src.redis_string import RedisString, Redis
import fakeredis
from loguru import logger
import src
import uuid

@pytest.fixture(autouse=True)
def redis_client(monkeypatch):
    client = fakeredis.FakeStrictRedis(decode_responses=True)
    monkeypatch.setattr(src, 'get_redis', lambda: client)
    return client