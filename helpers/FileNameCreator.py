import os
from datetime import datetime


class FileNameCreator:

    def get_file_path(self, server_name):
        backup_directory = os.path.dirname(os.getcwd() + "/Backups/" + server_name)
        self._directory_validation(backup_directory)
        destination = os.path.dirname(backup_directory + "/" + server_name + "/")
        self._directory_validation(destination)

        today_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        filename = (server_name + '___' + today_time + '.sql')

        return destination + "/" + filename

    @staticmethod
    def _directory_validation(dir_path):
        """
        Check if the directory is present, if not create this directory
        :param dir_path:
        :return:
        """
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
