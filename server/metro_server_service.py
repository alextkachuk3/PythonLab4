import Pyro4 as Pyro

from server.metro_server import MetroServer


class MetroServerService:
    def __init__(self, db_host, db_port, db_user, db_password, db_name):
        self.daemon = Pyro.Daemon()
        self.metro_server = MetroServer(db_host, db_port, db_user, db_password, db_name)
        self.uri = self.daemon.register(self.metro_server)
        self.ns = Pyro.locateNS()
        self.ns.register('metro', self.uri)

    def run(self):
        self.daemon.requestLoop()

    def stop(self):
        self.daemon.shutdown()
