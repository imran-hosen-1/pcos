from .base import Service


class PostgreSQLService(Service):
    def start(self):
        print(f"[START] PostgreSQL")

    def stop(self):
        print(f"[STOP] PostgreSQL")

    def status(self):
        return "unknown"