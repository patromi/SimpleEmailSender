from dotenv import load_dotenv
import os
import smtplib


class SMTPConnector:
    def __init__(self):
        load_dotenv()
        self._from_email = os.getenv("EMAIL")
        self._password = os.getenv("PASSWORD")
        self._subject = os.getenv("SUBJECT")
        self._port = int(os.getenv("PORT")) if os.getenv("PORT").isdigit() else 587
        self._host = os.getenv("HOST")
        self._server = None

    def _connect_to_server(self):
        self._server = smtplib.SMTP(self._host, self._port)
        self._server.starttls()
        self._server.login(self._from_email, self._password)

    def _disconnect_from_server(self):
        if self._server:
            self._server.quit()
            self._server = None
