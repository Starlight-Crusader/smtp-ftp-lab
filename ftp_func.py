from ftplib import FTP
from os import path


class FTPClient:

    def __init__(self, server_host, server_wd, username, password) -> None:
        self.server_host = server_host
        self.server_wd = server_wd
        self.username = username
        self.password = password

        self.ftp = FTP(self.server_host)
        self.ftp.login(self.username, self.password)
        self.ftp.cwd(self.server_wd)

    def upload(self, local_path) -> str:
        filename = [element for element in local_path.split(path.sep) if element][-1]

        with open(local_path, 'rb') as local_file:
            self.ftp.storbinary('STOR ' + filename, local_file)

        return f"ftp:://{self.username}:{self.password}@{self.server_host}{self.server_wd}{filename}"

    def delete(self, filename) -> None:
        self.ftp.delete(filename)
