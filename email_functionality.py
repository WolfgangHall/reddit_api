import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

# link account information dictionary file
sys.path.insert(0, r'D:\app')
from account_info import account


class SendEmail:

    my_email = account['email']

    def __init__(self, subject, body):
        self.msg = MIMEMultipart()
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.subject = subject
        self.body = body

        self.generate_msg(self.subject, self.body)
        self.create_server()

    def generate_msg(self, subject, body):
        self.msg['From'] = SendEmail.my_email
        self.msg['To'] = SendEmail.my_email
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(body, 'plain'))

    def create_server(self):
        self.server.starttls()
        self.server.login(SendEmail.my_email, account['email_password'])
        text = self.msg.as_string()
        self.server.sendmail(SendEmail.my_email, SendEmail.my_email, text)
        self.server.quit()
