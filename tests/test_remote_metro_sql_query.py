import unittest

from client.metro_client import MetroClient

client = MetroClient()


class TestRemoteMetroSQL(unittest.TestCase):

    def tearDown(self) -> None:
        client.reset_db()

    def test_adding_lines(self):
        client.add_line('green')
        client.add_line('red')
        client.add_line('blue')
        result = client.get_lines_list()
        print(result)

        self.assertEqual(result, [(1, 'green'), (2, 'red'), (3, 'blue')])

    def test_delete_lines(self):
        client.add_line('green')
        client.add_line('red')
        client.add_line('blue')
        client.delete_line(2)

        result = client.get_lines_list()
        print(result)

        self.assertEqual(result, [(1, 'green'), (3, 'blue')])

    def test_adding_station(self):
        client.add_line('green')
        client.add_line('red')
        client.add_line('blue')
        client.add_station('Teremky', 3, '6:00:00', '23:45:00')
        client.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        client.add_station('Vasylkivska', 3, '6:00:00', '23:45:00')
        client.add_station('Syrets', 1, '6:00:00', '23:40:00')
        client.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        client.add_station('Holosiivska', 3, '6:30:00', '23:45:00')
        client.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')
        client.add_station('Lukianivska', 1, '6:00:00', '23:40:00')
        client.add_station('Sviatoshyn', 2, '6:00:00', '23:30:00')
        client.add_station('Nykvy', 2, '6:00:00', '23:45:00')
        client.add_station('Zoloti Vorota', 1, '6:00:00', '23:40:00')
        client.add_station('Demiivska', 3, '6:00:00', '23:45:00')

        result_stations = client.get_list_of_stations()
        print(result_stations)

        self.assertEqual(result_stations,
                         [(1, 'Teremky', '6:00:00', '23:45:00', 3), (2, 'Vystavkovyi Tsentr', '6:00:00', '23:45:00', 3),
                          (3, 'Vasylkivska', '6:00:00', '23:45:00', 3), (4, 'Syrets', '6:00:00', '23:40:00', 1),
                          (5, 'Akademmistechko', '6:00:00', '23:45:00', 2),
                          (6, 'Holosiivska', '6:30:00', '23:45:00', 3), (7, 'Dorohozhychi', '6:00:00', '23:40:00', 1),
                          (8, 'Lukianivska', '6:00:00', '23:40:00', 1), (9, 'Sviatoshyn', '6:00:00', '23:30:00', 2),
                          (10, 'Nykvy', '6:00:00', '23:45:00', 2), (11, 'Zoloti Vorota', '6:00:00', '23:40:00', 1),
                          (12, 'Demiivska', '6:00:00', '23:45:00', 3)])

    def test_deleting_station(self):
        client.add_line('green')
        client.add_line('red')
        client.add_line('blue')
        client.add_station('Teremky', 3, '6:00:00', '23:45:00')
        client.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        client.add_station('Vasylkivska', 3, '6:00:00', '23:45:00')
        client.add_station('Syrets', 1, '6:00:00', '23:40:00')
        client.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        client.add_station('Holosiivska', 3, '6:30:00', '23:45:00')
        client.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')
        client.add_station('Lukianivska', 1, '6:00:00', '23:40:00')
        client.add_station('Sviatoshyn', 2, '6:00:00', '23:30:00')
        client.add_station('Nykvy', 2, '6:00:00', '23:45:00')
        client.add_station('Zoloti Vorota', 1, '6:00:00', '23:40:00')
        client.add_station('Demiivska', 3, '6:00:00', '23:45:00')

        client.delete_station(3)
        client.delete_station(5)
        client.delete_station(9)
        client.delete_station(4)

        result_stations = client.get_list_of_stations()
        print(result_stations)

        self.assertEqual(result_stations,
                         [(1, 'Teremky', '6:00:00', '23:45:00', 3), (2, 'Vystavkovyi Tsentr', '6:00:00', '23:45:00', 3),
                          (6, 'Holosiivska', '6:30:00', '23:45:00', 3), (7, 'Dorohozhychi', '6:00:00', '23:40:00', 1),
                          (8, 'Lukianivska', '6:00:00', '23:40:00', 1), (10, 'Nykvy', '6:00:00', '23:45:00', 2),
                          (11, 'Zoloti Vorota', '6:00:00', '23:40:00', 1), (12, 'Demiivska', '6:00:00', '23:45:00', 3)])

    def test_update_station(self):
        client.add_line('green')
        client.add_line('red')
        client.add_line('blue')
        client.add_station('Teremky', 3, '6:00:00', '23:45:00')
        client.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        client.add_station('Vasylkovska', 3, '6:00:00', '23:45:00')
        client.add_station('Syrets', 1, '6:00:00', '23:40:00')
        client.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        client.add_station('Holosivska', 3, '6:30:00', '23:45:00')
        client.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')

        client.update_station(3, 'Vasylkivska', 3, '5:00:00', '23:00:00')
        client.update_station(6, 'Holosiivska', 3, '5:30:00', '23:00:00')

        result = client.get_list_of_stations()
        print(result)

        self.assertEqual(result,
                         [(1, 'Teremky', '6:00:00', '23:45:00', 3), (2, 'Vystavkovyi Tsentr', '6:00:00', '23:45:00', 3),
                          (3, 'Vasylkivska', '5:00:00', '23:00:00', 3), (4, 'Syrets', '6:00:00', '23:40:00', 1),
                          (5, 'Akademmistechko', '6:00:00', '23:45:00', 2),
                          (6, 'Holosiivska', '5:30:00', '23:00:00', 3), (7, 'Dorohozhychi', '6:00:00', '23:40:00', 1)])

    def test_find_station_by_name(self):
        client.add_line('green')
        client.add_line('red')
        client.add_line('blue')
        client.add_station('Teremky', 3, '6:00:00', '23:45:00')
        client.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        client.add_station('Vasylkivska', 3, '6:00:00', '23:45:00')
        client.add_station('Syrets', 1, '6:00:00', '23:40:00')
        client.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        client.add_station('Holosiivska', 3, '6:30:00', '23:45:00')
        client.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')
        client.add_station('Lukianivska', 1, '6:00:00', '23:40:00')
        client.add_station('Sviatoshyn', 2, '6:00:00', '23:30:00')
        client.add_station('Nykvy', 2, '6:00:00', '23:45:00')
        client.add_station('Zoloti Vorota', 1, '6:00:00', '23:40:00')
        client.add_station('Demiivska', 3, '6:00:00', '23:45:00')

        result = client.find_station_by_name('Sviatoshyn')
        print(result)

        self.assertEqual(result, (9, 'Sviatoshyn', '6:00:00', '23:30:00', 2))

    def test_get_count_of_line_stations(self):
        client.add_line('green')
        client.add_line('red')
        client.add_line('blue')
        client.add_station('Teremky', 3, '6:00:00', '23:45:00')
        client.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        client.add_station('Vasylkivska', 3, '6:00:00', '23:45:00')
        client.add_station('Syrets', 1, '6:00:00', '23:40:00')
        client.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        client.add_station('Holosiivska', 3, '6:30:00', '23:45:00')
        client.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')
        client.add_station('Lukianivska', 1, '6:00:00', '23:40:00')
        client.add_station('Sviatoshyn', 2, '6:00:00', '23:30:00')
        client.add_station('Nykvy', 2, '6:00:00', '23:45:00')
        client.add_station('Zoloti Vorota', 1, '6:00:00', '23:40:00')
        client.add_station('Demiivska', 3, '6:00:00', '23:45:00')

        result = client.get_count_of_line_stations(3)
        print(result)

        self.assertEqual(result, 5)

    def test_get_list_of_line_stations(self):
        client.add_line('green')
        client.add_line('red')
        client.add_line('blue')
        client.add_station('Teremky', 3, '6:00:00', '23:45:00')
        client.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        client.add_station('Vasylkivska', 3, '6:00:00', '23:45:00')
        client.add_station('Syrets', 1, '6:00:00', '23:40:00')
        client.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        client.add_station('Holosiivska', 3, '6:30:00', '23:45:00')
        client.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')
        client.add_station('Lukianivska', 1, '6:00:00', '23:40:00')
        client.add_station('Sviatoshyn', 2, '6:00:00', '23:30:00')
        client.add_station('Nykvy', 2, '6:00:00', '23:45:00')
        client.add_station('Zoloti Vorota', 1, '6:00:00', '23:40:00')
        client.add_station('Demiivska', 3, '6:00:00', '23:45:00')

        result = client.get_line_stations_list(3)
        print(result)

        self.assertEqual(result, [(1, 'Teremky', '6:00:00', '23:45:00', 3),
                                  (2, 'Vystavkovyi Tsentr', '6:00:00', '23:45:00', 3),
                                  (3, 'Vasylkivska', '6:00:00', '23:45:00', 3),
                                  (6, 'Holosiivska', '6:30:00', '23:45:00', 3),
                                  (12, 'Demiivska', '6:00:00', '23:45:00', 3)])

    def test_get_list_of_lines(self):
        client.add_line('green')
        client.add_line('red')
        client.add_line('blue')
        client.add_station('Teremky', 3, '6:00:00', '23:45:00')
        client.add_station('Vystavkovyi Tsentr', 3, '6:00:00', '23:45:00')
        client.add_station('Vasylkivska', 3, '6:00:00', '23:45:00')
        client.add_station('Syrets', 1, '6:00:00', '23:40:00')
        client.add_station('Akademmistechko', 2, '6:00:00', '23:45:00')
        client.add_station('Holosiivska', 3, '6:30:00', '23:45:00')
        client.add_station('Dorohozhychi', 1, '6:00:00', '23:40:00')
        client.add_station('Lukianivska', 1, '6:00:00', '23:40:00')
        client.add_station('Sviatoshyn', 2, '6:00:00', '23:30:00')
        client.add_station('Nykvy', 2, '6:00:00', '23:45:00')
        client.add_station('Zoloti Vorota', 1, '6:00:00', '23:40:00')
        client.add_station('Demiivska', 3, '6:00:00', '23:45:00')

        result = client.get_lines_list()

        print(result)

        self.assertEqual(result, [(1, 'green'), (2, 'red'), (3, 'blue')])


if __name__ == '__main__':
    unittest.main()
