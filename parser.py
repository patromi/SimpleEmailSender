import pandas as pd
from jinja2 import Environment, FileSystemLoader
from iocontroller import IOController


class Parser(IOController):
    def __init__(self, template_file: str = 'template.txt', template_dir: str = '.'):
        self.template_file: str = template_file
        self.template_dir: str = template_dir

    @staticmethod
    def match_https_url(url) -> bool:
        return isinstance(url, str) and url.startswith('https://github.com/') and " " not in url

    def parse_data(self, path_csv: str, mode="template") -> pd.DataFrame:
        data: pd.DataFrame = self.open_csv(path_csv=path_csv)
        required_columns: list[str] = [
            'Technologia wybrana do wykonania zadnia rekrutacyjnego',
            'odpowiedz',
            'Link do repozytorium na githubie z wykonanym zadaniem rekrutacyjnym',
            'Adres e-mail',
            'Imię i Nazwisko',
        ]  # variable to change
        if not all(col in data.columns for col in required_columns):
            raise OSError(f"Error: CSV file is missing required columns.{data.columns}")

        if mode == "template":
            data['body'] = data.apply(self._generate_body, axis=1)
        elif mode == "custom_template":
            data['body'] = self.open_txt(self.template_file)
        return data

    def _generate_body(self, row: pd.Series) -> str:
        env: Environment = Environment(loader=FileSystemLoader(self.template_dir))
        template = env.get_template(self.template_file)
        return template.render(
            lang=row['Technologia wybrana do wykonania zadnia rekrutacyjnego'],
            link="discord",
            feedback=row["odpowiedz"],
            response=row["Link do repozytorium na githubie z wykonanym zadaniem rekrutacyjnym"],
            github=True if self.match_https_url(row['odpowiedz']) else False
        )
