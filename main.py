from ftp_func import FTPClient
from smtp_func import SMTPClient
from os import getenv

ftp = FTPClient(getenv('APP_FTP_SERVER_HOST'), getenv('APP_FTP_SERVER_WD'), getenv('APP_CLIENT_FTP_USER'), getenv('APP_CLIENT_FTP_PASS'))
url = ftp.upload(getenv('APP_CLIENT_TEST_PATH'), "tarnation2.img")

SMTPClient.send("Test Subject", "Test Body", url, "test.sender@gmail.com", getenv('APP_CLIENT_SMTP_EMAIL'))