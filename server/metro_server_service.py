import Pyro4

from server.metro_server import MetroServer


class MetroServerService:
    def __init__(self):
        self.daemon = Pyro4.Daemon()
        self.uri = self.daemon.register(MetroServer)
        self.ns = Pyro4.locateNS()
        self.ns.register('metro', self.uri)

    def run(self):
        self.daemon.requestLoop()

    def stop(self):
        self.daemon.shutdown()
