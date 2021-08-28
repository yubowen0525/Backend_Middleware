from src import Redis
import json

lua2 = """
    redis.call('del', KEYS[1])
    local exist = redis.call('exists',KEYS[1])
    if (exist == 0) then
        redis.call('HMSET', KEYS[1], unpack(ARGV))
        return 1
    end
    return 0
"""

data = {
    "1.2.3.4_wiki": json.dumps(
        [
            {
                "startTime": 1500000000,
                "endTime": 1600000000,
                "reason": "rule match.",
                "action": "allow",
            },
                        {
                "startTime": 1500000000,
                "endTime": 1600000000,
                "reason": "rule match.",
                "action": "allow",
            }
        ]
    ),
    "1.2.3.4_jira": json.dumps(
        [
            {
                "startTime": 1600000000,
                "endTime": 1600000000,
                "reason": "rule match.",
                "action": "block",
            },
                        {
                "startTime": 1600000000,
                "endTime": 1600000000,
                "reason": "rule match.",
                "action": "block",
            }
        ]
    ),
    "1.2.3.4_github": json.dumps(
        [
            {
                "startTime": 1600000000,
                "endTime": 1600000000,
                "reason": "rule match.",
                "action": "monitor",
            },
                        {
                "startTime": 1600000000,
                "endTime": 1600000000,
                "reason": "rule match.",
                "action": "monitor",
            }
        ]
    )
}


class RedisLua(Redis):
    def script(self):
        script = self._redis_client.register_script(lua2)
        res = []
        for k, v in data.items():
            res.append(k)
            res.append(v)
        call = script(keys=["my_test"],args=res)
        print(self._redis_client.hgetall("my_test"))
        
        
        

if __name__ == '__main__':
    lua = RedisLua()
    lua.script()