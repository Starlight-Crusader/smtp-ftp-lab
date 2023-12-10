from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText
from os import getenv


class SMTPClient:

    def send(subject, msg, attachment, from_addr, to_addr) -> bool:
        message = MIMEText("<div class='msg'>" + msg + "</div><br><div class='attachment'>" + attachment + "</div>", "html")
        
        message['Subject'] = subject
        message['From'] = from_addr
        message['To'] = to_addr

        try:
            with SMTP(getenv('APP_SMTP_SERVER_HOST'), getenv('APP_SMTP_SERVER_PORT')) as server:
                server.starttls()
                server.login(getenv('APP_CLIENT_SMTP_EMAIL'), getenv('APP_CLIENT_SMTP_PASS'))
                server.sendmail(from_addr, to_addr, message.as_string())
                server.quit()
                return True

        except SMTPException as error:
            print(f'Email server error: {error}')
            return False