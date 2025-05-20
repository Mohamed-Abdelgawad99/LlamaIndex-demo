from common.imports import *


class FileLoader:
    def read_file(file_path):
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        else:
            print(f"Warning: File not found -> {file_path}")
            return None
