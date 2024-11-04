import os

from sender import Sender
from parser import Parser


class Main:
    def __init__(self, path_csv: str):
        self.data = Parser().parse(path_csv)
        self.sender = Sender()

    def run(self) -> None:
        self.sender.process_and_send_emails(self.data)


if __name__ == "__main__":
    main = Main(os.getenv("CSV_PATH"))
    main.run()
