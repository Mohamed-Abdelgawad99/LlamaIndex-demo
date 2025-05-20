from common.imports import *


class JsonSaver:
    @staticmethod
    def generate_output_path(input_json_path):
        """Generating json file path by addin processed to the file name"""
        base, ext = os.path.splitext(input_json_path)
        return base + "_processed" + ext

    @staticmethod
    def save_json(data, input_json_path):
        """Saving the new data processed to a new json file at the same path as the input file"""
        output_json_path = JsonSaver.generate_output_path(input_json_path)
        with open(output_json_path, "w") as file:
            json.dump(data, file, indent=4)
        return output_json_path
        print(f"The Updated JSON file is ready at -> {output_json_path}")
