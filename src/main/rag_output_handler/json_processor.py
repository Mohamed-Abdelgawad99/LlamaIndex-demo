from common.imports import *
from .file_loader import FileLoader


class JsonProcessor:
    """Handels processing Json file output from the RAG team part"""

    def __init__(self, input_json_path):
        self.input_json_path = input_json_path
        self.data = None

    def load_json(self):
        try:
            with open(self.input_json_path, "r", encoding="utf-8") as file:
                self.data = json.load(file)
                print("I am here")

            if self.data is None:
                raise ValueError(f"The json file {self.input_json_path} is empty")

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except FileNotFoundError:
            print(f"File not found: -> {self.input_json_path}")
        except ValueError as ve:
            print(ve)

    def process_usecases(self):
        """For processing covered usecases and addin the files contents"""
        for usecase, details in self.data.items():
            if usecase != "description":
                if details.get("status") == "covered" and "files" in details:
                    for file_key, file_info in details["files"].items():
                        file_path = file_info.get("path")
                        if file_path:
                            file_contents = FileLoader.read_file(file_path)
                            if file_contents is not None:
                                self.data[usecase]["files"][file_key]["contents"] = (
                                    file_contents
                                )

    def get_proessed_data(self):
        """
        Returns:
            json format data: the updated data after processing
        """
        return self.data
