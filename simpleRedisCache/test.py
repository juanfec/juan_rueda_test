import fakeredis
import unittest
from simplecache import SimpleRedisCache
import time

class TestRedisCache(unittest.TestCase):
    def setUp(self):
        server = fakeredis.FakeServer()
        self.redis = fakeredis.FakeStrictRedis(server=server, decode_responses=True)

    def testCache(self):
        cache = SimpleRedisCache(ttl=60)
        cache.set_redis_conn(self.redis)
        cache.set('1', 'uno')
        self.assertEqual(cache.get('1'), 'uno')

    def testCacheTtl(self):
        cache = SimpleRedisCache(ttl=1)
        cache.set_redis_conn(self.redis)
        cache.set('1', '1')
        self.assertEqual(cache.get('1'), '1')
        time.sleep(1)
        self.assertEqual(cache.get('1'), None)

    def testCacheDelete(self):
        cache = SimpleRedisCache(ttl=60)
        cache.set_redis_conn(self.redis)
        cache.set('1', 'uno')
        self.assertEqual(cache.get('1'), 'uno')
        cache.delete('1')
        self.assertEqual(cache.get('1'), None)
    
    def testCacheHset(self):
        cache = SimpleRedisCache(ttl=60)
        cache.set_redis_conn(self.redis)
        cache.hset('1', {'uno':'1'})
        self.assertEqual(cache.hget('1','uno'), '1')

if __name__ == '__main__':
    unittest.main()