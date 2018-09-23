import os
import subprocess

from helpers.utils import Database


class DetectDatabase:
    def __init__(self, name="postgres"):
        if name is not None:
            lowercase_name = name.lower()
            if lowercase_name == "postgres":
                self.database = Database.postgresql
            elif lowercase_name == "mysql":
                self.database = Database.mysql
            elif lowercase_name == "mongo" or lowercase_name == "mongodb":
                self.database = Database.mongodb
            elif lowercase_name == "oracle" or lowercase_name == "oracledb":
                self.database = Database.oracle
            elif lowercase_name == "mssql" or lowercase_name == "microsoft" or lowercase_name == "microsoft sql server" or lowercase_name == "ms sql" or lowercase_name == "ms sql server":
                self.database = Database.mssql
            else:
                self.database = Database.postgresql
        else:
            self.database = Database.postgresql

    def __str__(self) -> str:
        return super().__str__()


class DatabaseBackup:
    def __init__(self, server, filename) -> None:
        super().__init__()
        self.server = server
        self.filename = filename
        self._start_backup()

    def __str__(self) -> str:
        return super().__str__()

    def _start_backup(self):
        if DetectDatabase(self.server.type).database == Database.postgresql:
            self._postgres_backup()

    def _mysql_backup(self):
        p = subprocess.Popen(
                ['mysqldump', '-f', '-h', self.server.host, '--password=' + self.server.password,
                 '-P', str(self.server.port), '-u', self.server.user_name, '-v', '--all-databases',
                 '>', self.filename])
        p.communicate()

    def _postgres_backup(self):
        os.putenv('PGPASSWORD', self.server.password)
        p = subprocess.Popen(
                ['pg_dump', '-h', self.server.host, '-p', str(self.server.port), '-U',
                 self.server.user_name, '-Fp', self.server.database, '-C', '-f', self.filename])
        p.communicate()
