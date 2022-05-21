import Pyro4 as Pyro

ns = Pyro.locateNS()
uri = ns.lookup('metro')
o = Pyro.Proxy(uri)
print(o.get_lines_list())
