import os
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
class Sender:
    def __init__(self):
        load_dotenv()
        self._from_email = os.getenv("EMAIL")
        self._password = os.getenv("PASSWORD")
        self._subject = os.getenv("SUBJECT")
        self._server = None

    def _connect_to_server(self):
        self._server = smtplib.SMTP('smtp.gmail.com', 587)
        self._server.starttls()
        self._server.login(self._from_email, self._password)

    def _disconnect_from_server(self):
        if self._server:
            self._server.quit()
            self._server = None

    def process_and_send_emails (self, data: pd.DataFrame):
        self._connect_to_server()
        for _, row in data.iterrows():
            if not row.get("body"):
                continue

            template = self._create_template(row)
            self._send(template)
        self._disconnect_from_server()

    def _create_template(self, row: pd.Series) -> MIMEMultipart:
        msg = MIMEMultipart()
        msg['From'] = self._from_email
        msg['To'] = row['Adres e-mail']
        msg['Subject'] = self._subject
        message = row["body"]
        msg.attach(MIMEText(message, 'plain'))
        return msg

    def _send(self, msg: MIMEMultipart) -> None:
        try:
            self._server.sendmail(self._from_email, msg['To'], msg.as_string())
            print("Email sent successfully to", msg['To'])
        except Exception as e:
            print(f"Error sending email to {msg['To']}: {e}")
