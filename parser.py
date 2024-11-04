import pandas as pd
from jinja2 import Environment, FileSystemLoader


class Parser:
    def __init__(self, template_file='template.txt', template_dir='.'):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template(template_file)

    @staticmethod
    def match_https_url(url) -> bool:
        return isinstance(url, str) and url.startswith('https://github.com/') and " " not in url

    def parse(self, path_csv) -> pd.DataFrame:
        try:
            data = pd.read_csv(path_csv)
        except FileNotFoundError:
            print(f"Error: File {path_csv} not found.")
            return pd.DataFrame()

        required_columns = [
            'Technologia wybrana do wykonania zadnia rekrutacyjnego',
            'odpowiedz',
            'Link do repozytorium na githubie z wykonanym zadaniem rekrutacyjnym',
            'Adres e-mail',
            'Imię i Nazwisko',
        ]
        if not all(col in data.columns for col in required_columns):
            raise OSError(f"Error: CSV file is missing required columns.{data.columns}")

        data['body'] = data.apply(self._generate_body, axis=1)
        return data

    def _generate_body(self, row):

        return self.template.render(
            lang=row['Technologia wybrana do wykonania zadnia rekrutacyjnego'],
            link="discord",
            feedback=row["odpowiedz"],
            response=row["Link do repozytorium na githubie z wykonanym zadaniem rekrutacyjnym"],
            github=True if self.match_https_url(row['odpowiedz']) else False
        )
