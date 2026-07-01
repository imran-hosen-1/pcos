from .base import Service


class RedisService(Service):
    def start(self):
        print(f"[START] Redis")

    def stop(self):
        print(f"[STOP] Redis")

    def status(self):
        return "unknown"