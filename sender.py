import os
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from connector import SMTPConnector
from logger import Logger


class Sender(SMTPConnector, Logger):
    def __init__(self):
        super().__init__()

    def process_and_send_emails(self, data: pd.DataFrame):
        self._connect_to_server()
        for _, row in data.iterrows():
            if not row.get("body"):
                continue

            template: MIMEMultipart = self._create_mail_template(row)
            self._send_mail(template)
        self._disconnect_from_server()

    def _create_mail_template(self, row: pd.Series) -> MIMEMultipart:
        msg: MIMEMultipart = MIMEMultipart()
        msg['From'] = self._from_email
        msg['To'] = row['Adres e-mail']
        msg['Subject'] = self._subject
        message = row["body"]
        msg.attach(MIMEText(message, 'plain'))
        return msg

    def _send_mail(self, msg: MIMEMultipart) -> None:
        try:
            self._server.sendmail(self._from_email, msg['To'], msg.as_string())
            self.log_sent_email(msg['To'], msg['body'])
            print("Email sent successfully to", msg['To'])
        except Exception as e:
            self.log_error(msg['To'], e)
            print(f"Error sending email to {msg['To']}: {e}")
