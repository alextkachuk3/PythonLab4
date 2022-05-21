from test_config import db_host, db_port, db_user, db_password, db_name
from server.metro_server_service import MetroServerService

server_service = MetroServerService(db_host, db_port, db_user, db_password, db_name)
server_service.run()
