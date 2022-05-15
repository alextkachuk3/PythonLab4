import Pyro4
ns = Pyro4.locateNS()
uri = ns.lookup('metro')
o = Pyro4.Proxy(uri)
print(o.get_line_list())
