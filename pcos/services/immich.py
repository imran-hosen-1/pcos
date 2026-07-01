from pcos.services.base import Service


class ImmichService(Service):

    def start(self):
        pass

    def stop(self):
        pass

    def restart(self):
        pass

    def status(self):
        return "unknown"

    def health(self):
        return {}