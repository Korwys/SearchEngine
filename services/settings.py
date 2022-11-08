import redis


class SettingManager:
    redis = redis.Redis(host='localhost', port=6379, db=0)


manager = SettingManager()