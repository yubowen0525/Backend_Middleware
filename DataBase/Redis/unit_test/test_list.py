from unit_test.base import *
from src.list import RedisList


@pytest.mark.parametrize(
    "input, output",
    [
        (
            {"key": "test_" + str(uuid.uuid4()), "value": ("1","2","3","4")},
            "v_1",
        ),
        (
            {"key": "test_" + str(uuid.uuid4()), "value": ("1","2","3","4","5","6")},
            "v_2",
        ),
    ],
)
def test_list_FIFO(input, output):
    m_list = RedisList(input["key"])
    flag = m_list.lpush(*input["value"])
    print("lpush:", flag)
    flag = m_list.lindex(0)
    print("lindex_0:", flag)
    flag = m_list.lrange(0, 3)
    print("lrange_0_3:", flag)
    flag = m_list.lrange(0, 8)
    print("lrange_0_8:", flag)
    flag = m_list.rpop()
    print("lpop:", flag)
    flag = m_list.rpop()
    print("lpop:", flag)
    flag = m_list.lindex(0)
    print("lindex_0:", flag)
    flag = m_list.lrange(0, 3)
    print("lrange_0_3:", flag)
    flag = m_list.lrange(0, 8)
    print("lrange_0_8:", flag)
    
@pytest.mark.parametrize(
    "input, output",
    [
        (
            {"key": "test_" + str(uuid.uuid4()), "value": ("1","2","3","4")},
            "v_1",
        ),
        (
            {"key": "test_" + str(uuid.uuid4()), "value": ("1","2","3","4","5","6")},
            "v_2",
        ),
    ],
)
def test_list_FIFO(input, output):
    m_list = RedisList(input["key"])
    flag = m_list.lpush(*input["value"])
    print("lpush:", flag)
    
    print("len", len(m_list))
    print("slice", m_list[:-1])
    