class Server:
    def __init__(self, url=None, port=None, db_name=None, username=None, password=None, server_name=None):
        self.connection_string = "host='" + url + "' port='" + str(
            port) + "' dbname='" + db_name + "' user='" + username + "' password='" + password + "'"

        self.server_name = server_name
        self.user_name = username
        self.password = password
        self.host = url
        self.database = db_name
        self.port = port

    def __str__(self) -> str:
        return super().__str__()
