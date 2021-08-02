import pytest
from src.redis_string import RedisString
from loguru import logger
import uuid

@pytest.mark.parametrize(
    "input, output",
    [
        (
            {"key": str(uuid.uuid4()), "value": "v_1"},
            "v_1",
        ),
        (
            {"key": str(uuid.uuid4()), "value": "v_2"},
            "v_2",
        ),
    ],
)
def test_string_set_get(input, output):
    c_str = RedisString()
    flag = c_str.set(key=input["key"], value=input["value"], ex=10)
    print("flag:", flag)
    v = c_str.get(input["key"]).decode()
    assert v == output


@pytest.mark.parametrize(
    "input",
    [
        (
            {"key": str(uuid.uuid4()), "value": "v_1"}
        ),
        (
            {"key": str(uuid.uuid4()), "value": "v_2"}
        ),
    ],
)
def test_string_setnx_delete(input):
    c_str = RedisString()
    flag1 = c_str.set(key=input["key"], value=input["value"], nx=True, ex=10)
    print("set_flag1: %s" % (flag1))
    flag2 = c_str.set(key=input["key"], value=input["value"], nx=True, ex=10)
    print("set_flag2: %s" % (flag2))
    assert flag1 != flag2
    flag3 = c_str.delete(input["key"])
    print("delete_flag3: %s" % str(flag3))