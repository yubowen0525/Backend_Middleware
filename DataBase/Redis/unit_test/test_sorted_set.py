import re
from unit_test.base import *
import uuid
from src.sorted_set import RedisSortedSet
import math

@pytest.mark.parametrize(
    "input, output",
    [
        (
            {
                "key": "test_" + str(uuid.uuid4()),
                "value": {"a": 1, "b": 2, "c": 3, "d": 4, "e":5, "f":6},
            },
            "v_1",
        ),
        (
            {
                "key": "test_" + str(uuid.uuid4()),
                "value": {"a": 1, "b": 1, "c": 1, "d": 2, "e":2, "f":2},
            },
            "v_2",
        ),
    ],
)
def test_sorted_set(input, output):
    def sqrt(v):
        return math.sqrt(float(v))
    m_sorted_set = RedisSortedSet(input["key"])
    flag = m_sorted_set.zadd(input["value"])
    print("zadd:", flag)
    assert flag == 6
    flag = m_sorted_set.zrange(start=0, end=-1)
    print("zrange:", flag)
    flag = m_sorted_set.zrange(start=0, end=-1, desc=True)
    print("zrange_desc:", flag)
    flag = m_sorted_set.zrangebylex('-', '[c')
    print("zrangebylex", flag)
    flag = m_sorted_set.zrangebyscore(0, 6, withscores=True, score_cast_func=sqrt)
    print("zrangebyscore:", flag)
    
