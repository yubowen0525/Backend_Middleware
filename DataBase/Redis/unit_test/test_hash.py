from unit_test.base import *
from src.hash import RedisHash


@pytest.mark.parametrize(
    "input, output",
    [
        (
            {"key": "test_" + str(uuid.uuid4()), "company1": 0, "company2": 0, "company3": 0},
            "v_1",
        ),
        (
            {"key": "test_" + str(uuid.uuid4()), "value": ("1","2","3","4","5","6")},
            "v_2",
        ),
    ],
)
def test_hash(input, output):
    m_hash = RedisHash(input["key"])
    flag = m_hash.hincrby("company1")
    print("hincrby:", flag)
    flag = m_hash.hincrby("company1")
    print("hincrby:", flag)
    flag = m_hash.hget("company1")
    print("get:", flag)
    
    