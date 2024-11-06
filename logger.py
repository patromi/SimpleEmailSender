import logging
from datetime import datetime


class Logger:
    def __init__(self, log_file="log.txt"):
        self.log_file = log_file

    def log_sent_email(self, email, body):
        logging.basicConfig(filename="log.txt", level=logging.INFO)
        logging.info(f"Email sent successfully to {email}, on {datetime.now()}, with body {body}")

    def log_error(self, email, error):
        logging.basicConfig(filename='log.txt', level=logging.ERROR)
        logging.error(f"Error sending email to {email}: {error}, on {datetime.now()}")
