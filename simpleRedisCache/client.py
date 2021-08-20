from simplecache import SimpleRedisCache

red = SimpleRedisCache('test.oj7u39.0001.use1.cache.amazonaws.com',6379)
red.set('a','a')
print(red.get('a'))