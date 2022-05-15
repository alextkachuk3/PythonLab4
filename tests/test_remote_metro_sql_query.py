import threading
import unittest

import Pyro4 as Pyro4

from client.metro_client import MetroClient
from server.metro import Metro
from server.metro_server_service import MetroServerService

from test_config import db_host, db_port, db_user, db_password, db_name


class TestRemoteMetroSQL(unittest.TestCase):
    def init(self):
        self.server = MetroServerService()
        self.th = threading.Thread(target=self.server.run)
        self.th.start()
        self.client = MetroClient()
        self.client.connect_to_db(db_host, db_port, db_user, db_password, db_name)
        self.metro = Metro(db_host, db_port, db_user, db_password, db_name)

    def end(self):
        self.metro.connection.cursor().execute("DROP TABLE metro_lines, metro_stations")
        self.server.stop()
        self.th.join()

    def test_adding_lines(self):
        self.init()

        self.client.add_line('green')
        self.client.add_line('red')
        self.client.add_line('blue')

        self.metro.connection.commit()
        result = self.metro.get_lines_list()
        print(result)

        self.end()

        self.assertEqual(result, [(1, 'green'), (2, 'red'), (3, 'blue')])


if __name__ == '__main__':
    unittest.main()
