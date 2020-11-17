import redis
from redis_lock import RedisLock
REDIS_SERVER = 'redis://:xxxxxx@19xxxx:6379/0'

conn = redis.Redis(host='19xxxxxx.13',port=6379,password='xxxx')

lock = RedisLock(conn,"redddxx")

import time
# time.sleep(1)
# lock.release()
try:
    re = lock.acquire()
    if re:
        print("locked")
    else:
        print('blocked')
    print(1)
    time.sleep(100000)
except KeyboardInterrupt:
    lock.release()
except:
    lock.release()
finally:
    lock.release()

