import Pyro4 as Pyro

ns = Pyro.locateNS()
uri = ns.lookup('metro')
o = Pyro.Proxy(uri)
print(o.get_lines_list())
print(o.get_count_of_line_stations(3))

print(o.get_lines_list())