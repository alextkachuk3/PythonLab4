import Pyro4 as Pyro4
from metro_server import MetroServer

daemon = Pyro4.Daemon()
uri = daemon.register(MetroServer)
ns = Pyro4.locateNS()
ns.register('metro', uri)
daemon.requestLoop()
