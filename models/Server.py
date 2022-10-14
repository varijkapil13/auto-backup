import logging

class Server:
    def __init__(self, url=None, port=None, db_name=None, username=None, password=None, server_name=None,
                 database_type="postgres"):
        log = logging.getLogger()
        log.setLevel(logging.INFO)

        log.info("Hosts: " + url)
        log.info("Ports: " + str(port))
        log.info("Database Name: " + db_name)
        log.info("Database Type: " + database_type)

        self.connection_string = "host='" + url + "' port='" + str(
                port) + "' dbname='" + db_name + "' user='" + username + "' password='" + password + "'" \
                                 + "' Database Type='" + database_type + "'"

        self.server_name = server_name
        self.user_name = username
        self.password = password
        self.host = url
        self.database = db_name
        self.port = port
        self.type = database_type

    def __str__(self) -> str:
        return super().__str__()
