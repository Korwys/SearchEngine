import redis

redis_test_manager = redis.Redis(host='localhost', port=6379, db=0)


def test_redis_cache():
    redis_test_manager.set('ззкзк', 'дддд')
    redis_response = redis_test_manager.get('ззкзк')
    new = redis_response.decode('utf-8')
    assert new == 'дддд'
