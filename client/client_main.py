import Pyro4

from config import db_host, db_port, db_user, db_password, db_name

ns = Pyro4.locateNS()
uri = ns.lookup('metro')
o = Pyro4.Proxy(uri)
o.connect_to_db(db_host, db_port, db_user, db_password, db_name)
print(o.get_lines_list())
