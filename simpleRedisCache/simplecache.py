import redis as redis

class SimpleRedisCache(object):
    def __init__(self, host='localhost', port=6379,ttl=0,db=0):
        self.redis = redis.Redis(host=host,port=port,db=db,)
        self.ttl = ttl

    def set_redis_conn(self, conn: redis) -> None:
        self.redis = conn

    def get(self, key: str) -> str:
        return self.redis.get( key)
    
    def hget(self, name: str,key: str) -> str:
        return self.redis.hget(name,key=key)

    def set(self, key: str, value: str) -> None:
        self.redis.set( key, value)
        self.exp(key)

    def hset(self, key: str,field:str, value: str) -> None:
        self.redis.hset(key,field,value)
        self.exp(key)

    def hset(self, key: str,mapping:dict) -> None:
        self.redis.hmset(key,mapping=mapping)
        self.exp(key)

    def delete(self, key):
        self.redis.delete(key)
        return True

    def clear(self) -> any:
        return self.redis.flushdb()
    
    def exp(self,key):
        if self.ttl!=0:
            self.redis.expire(key,self.ttl)

