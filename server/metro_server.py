import Pyro4 as Pyro4

from server.metro import Metro


@Pyro4.expose
class MetroServer:
    def __init__(self):
        self.metro = None

    def connect_to_db(self, db_host, db_port, db_user, db_password, db_name):
        self.metro = Metro(db_host, db_port, db_user, db_password, db_name)

    def add_line(self, color: str):
        self.metro.add_line(color)

    def delete_line(self, line_id: int):
        self.metro.delete_line(line_id)

    def add_station(self, name: str, line_id: int, open_time: str, close_time: str):
        self.metro.add_station(name, line_id, open_time, close_time)

    def delete_station(self, station_id: int):
        self.metro.delete_station(station_id)

    def update_station(self, station_id: int, name: str, line_id: int, open_time: str, close_time: str):
        self.metro.update_station(station_id, name, line_id, open_time, close_time)

    def find_station_by_name(self, name: str):
        return self.metro.find_station_by_name(name)

    def get_count_of_line_stations(self, line_id: int):
        return self.metro.get_count_of_line_stations(line_id)

    def get_line_stations_list(self, line_id: int):
        return self.metro.get_line_stations_list(line_id)

    def get_lines_list(self):
        return self.metro.get_lines_list()
