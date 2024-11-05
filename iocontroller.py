import pandas as pd


class IOController:
    @staticmethod
    def open_csv(path_csv: str) -> pd.DataFrame:
        try:
            data: pd.DataFrame = pd.read_csv(path_csv)
            return data
        except FileNotFoundError:
            raise IOError(f"Error: File {path_csv} not found.")
        except Exception as e:
            raise Exception(f"Error: {e}")

    @staticmethod
    def open_txt(custom_template_path: str) -> str:
        try:
            with open(custom_template_path) as f:
                data = f.read()
        except FileNotFoundError:
            raise IOError(f"Error: File {custom_template_path} not found.")
        except Exception as e:
            raise Exception(f"Error: {e}")

        return data

