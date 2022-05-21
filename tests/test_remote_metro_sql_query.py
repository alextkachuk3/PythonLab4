import threading
import unittest

from client.metro_client import MetroClient
from server.metro import Metro
from server.metro_server_service import MetroServerService

from test_config import db_host, db_port, db_user, db_password, db_name

client = MetroClient()
metro = Metro(db_host, db_port, db_user, db_password, db_name)


class TestRemoteMetroSQL(unittest.TestCase):

    def tearDown(self) -> None:
        metro.connection.cursor().execute("DROP TABLE metro_lines, metro_stations")
        metro.connection.commit()
        metro.init_tables()

    def test_adding_lines(self):
        client.add_line('green')
        client.add_line('red')
        client.add_line('blue')
        metro.connection.commit()
        result = metro.get_lines_list()
        print(result)

        self.assertEqual(result, [(1, 'green'), (2, 'red'), (3, 'blue')])

    def test_delete_lines(self):
        client.add_line('green')
        client.add_line('red')
        client.add_line('blue')
        client.delete_line(2)

        metro.connection.commit()
        result = metro.get_lines_list()
        print(result)

        self.assertEqual(result, [(1, 'green'), (3, 'blue')])

    def test_adding_station(self):
        pass

    def test_deleting_station(self):
        pass

    def test_update_station(self):
        pass

    def test_search_station_by_name(self):
        pass

    def test_get_count_of_line_stations(self):
        pass

    def test_get_list_of_line_stations(self):
        pass

    def test_get_list_of_lines(self):
        pass


if __name__ == '__main__':
    unittest.main()
