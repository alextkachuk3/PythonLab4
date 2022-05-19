import threading
import unittest

import Pyro4 as Pyro4

from client.metro_client import MetroClient
from server.metro import Metro
from server.metro_server_service import MetroServerService

from test_config import db_host, db_port, db_user, db_password, db_name


class TestRemoteMetroSQL(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.server = MetroServerService()
        cls.th = threading.Thread(target=cls.server.run)
        cls.th.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.stop()
        cls.th.join()

    def setUp(self) -> None:
        self.client = MetroClient()
        self.client.connect_to_db(db_host, db_port, db_user, db_password, db_name)
        self.metro = Metro(db_host, db_port, db_user, db_password, db_name)

    def tearDown(self) -> None:
        self.metro.connection.cursor().execute("DROP TABLE metro_lines, metro_stations")

    def restart_metro_tables(self):
        self.metro.connection.cursor().execute("DROP TABLE metro_lines, metro_stations")
        self.metro.connection.commit()
        self.metro.init_tables()

    def test_adding_lines(self):
        self.client.add_line('green')
        self.client.add_line('red')
        self.client.add_line('blue')
        self.metro.connection.commit()

        result = self.metro.get_lines_list()
        print(result)

        self.assertEqual(result, [(1, 'green'), (2, 'red'), (3, 'blue')])

    def test_delete_lines(self):
        self.client.add_line('green')
        self.client.add_line('red')
        self.client.add_line('blue')
        self.client.delete_line(2)

        self.metro.connection.commit()
        result = self.metro.get_lines_list()
        print(result)

        self.assertEqual(result, [(1, 'green'), (3, 'blue')])


if __name__ == '__main__':
    unittest.main()
