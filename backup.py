import logging
import os
import subprocess
import configparser
import schedule
from daemon import runner

from models.Server import Server
from helpers.FileNameCreator import FileNameCreator

log = logging.getLogger()
log.setLevel(logging.INFO)

CONFIG_FILE_PATH = "servers.ini"


def start_backup():
    """

    :return:
    """
    connection_strings = self._read_db_configuration()

    print("Found the following connection strings\n -> %s" % connection_strings)

    for string in connection_strings:
        _create_backup(string)


def _read_db_configuration():
    """

    :return: Database Connection string
    """
    config_file = configparser.ConfigParser()
    config_file.read(CONFIG_FILE_PATH)
    connection_strings = []
    for section in config_file.sections():
        database_config = config_file[section]
        username = database_config.get('username')
        password = database_config.get('password')
        url = database_config.get('url')
        port = database_config.getint('port')
        db_name = database_config.get('database')

        if username is None or password is None or url is None or port is None or db_name is None:

            log.error(
                "One of the entries were not valid Please check the values and enter them in the following format: "
                "\n eg. \n[Database] \nurl = localhost\nport = 1521\nusername = testuser\npassword = "
                "sales\ndatabase = "
                "xe\n")
            log.error("Skipping backup for this database")
        else:
            connection_strings.append(Server(url, port, db_name, username, password, section))

    return connection_strings


def _create_backup(server):
    """

    :param server:
    :return:
    """
    file_name = FileNameCreator().get_file_path(server.server_name)

    os.putenv('PGPASSWORD', server.password)

    p = subprocess.Popen(
        ['pg_dump', '-h', server.host, '-p', str(server.port), '-U',
         server.user_name, '-Fp', server.database, '-C', '-f', file_name])
    p.communicate()


if __name__ == '__main__':
    schedule.every(3).minutes.do(start_backup)
    while True:
        schedule.run_pending()
