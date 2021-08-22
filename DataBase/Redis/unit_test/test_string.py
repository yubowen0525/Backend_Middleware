from unit_test.base import *
import src
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
    v = c_str.get(input["key"])
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
    
    

@pytest.mark.parametrize(
    "input, output",
    [
        (
            {"key1": 10, "key2":2, "key3":3, "key4":4},
            {"key1": 10, "key2":2, "key3":3, "key4":4},
        ),
        (
            {"key5": 500, "key6":6, "key7":7, "key8":8},
            {"key5": 500, "key6":6, "key7":7, "key8":8},
        ),
    ],
)
def test_string_sets_gets(input:dict, output):
    c_str = RedisString()
    flag = c_str.sets(input)
    print("sets_return:", flag)
    flag = c_str.gets(list(input.keys()))
    print("gets_return:", flag)
    flag = c_str.incr(list(input.keys())[0])
    print("incr_return:", flag)
    flag = c_str.decr(list(input.keys())[0])
    print("decr_return:", flag)
    flags = [c_str.get_bit(list(input.keys())[0], offset=i) for i in range(32)]
    print("get_bit_return:", flags)
    flag = c_str.get_len(list(input.keys())[0])
    print("len_return:", flag)
