from ftplib import FTP


class FTPClient:

    def __init__(self, server_host, server_wd, username, password) -> None:
        self.server_host = server_host
        self.server_wd = server_wd
        self.username = username
        self.password = password

        self.ftp = FTP(self.server_host)
        self.ftp.login(self.username, self.password)
        self.ftp.cwd(self.server_wd)

    def upload(self, path, filename) -> str:
        with open(path, 'rb') as local_file:
            self.ftp.storbinary('STOR ' + filename, local_file)

        return f"ftp:://{self.username}:{self.password}@{self.server_host}{self.server_wd}{filename}"

    def delete(self, filename) -> None:
        self.ftp.delete(filename)
