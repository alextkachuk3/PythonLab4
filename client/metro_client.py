import Pyro4


class MetroClient:
    def __init__(self):
        self.ns = Pyro4.locateNS()
        self.uri = self.ns.lookup('metro')
        self.o = Pyro4.Proxy(self.uri)

    def connect_to_db(self, db_host, db_port, db_user, db_password, db_name):
        self.o.connect_to_db(db_host, db_port, db_user, db_password, db_name)

    def add_line(self, name: str):
        self.o.add_line(name)

    def delete_line(self, line_id: int):
        self.o.delete_line(line_id)

    def add_station(self, name: str, line_id: int, open_time: str, close_time: str):
        self.o.add_station(name, line_id, open_time, close_time)

    def delete_station(self, station_id: int):
        self.o.delete_station(station_id)

    def update_station(self, station_id: id, name: str, line_id: int, open_time: str, close_time: str):
        self.o.update_station(station_id, name, line_id, open_time, close_time)

    def find_station_by_name(self, name: str):
        return self.o.find_station_by_name(name)

    def get_count_of_line_stations(self, line_id):
        return self.o.get_count_of_line_stations(line_id)

    def get_line_stations_list(self, line_id):
        return self.o.get_line_stations_list(line_id)

    def get_lines_list(self):
        return self.o.get_lines_list()
