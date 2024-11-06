import os

from sender import Sender
from parser import Parser
from dotenv import load_dotenv

class Main:
    def __init__(self, path_csv: str, mode: str = "template", template_path: str = None):
        self.data = Parser(template_file=template_path).parse_data(path_csv=path_csv, mode=mode)
        self.sender = Sender()

    def run(self) -> None:
        self.sender.process_and_send_emails(self.data)


if __name__ == "__main__":
    load_dotenv()
    mode = os.getenv("MODE").lower()
    csv_path = os.getenv("CSV_PATH")
    template_path = os.getenv("TEMPLATE_PATH")

    print(f"Mode: {mode}")
    print(f"CSV Path: {csv_path}")
    print(f"Template Path: {template_path}")

    if mode not in ["template", "custom_template"]:
        raise ValueError("Invalid mode. Please choose 'template' or 'custom_template'.")

    main = Main(path_csv=os.getenv("CSV_PATH"), mode=mode, template_path=os.getenv("TEMPLATE_PATH"))

    main.run()
