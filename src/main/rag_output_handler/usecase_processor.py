from json_processor import JsonProcessor
from json_saver import JsonSaver


def process_rag_output(input_json_path):
    processor = JsonProcessor(input_json_path)
    processor.load_json()
    processor.process_usecases()

    updated_data = processor.get_proessed_data()
    JsonSaver.save_json(updated_data, input_json_path)


if __name__ == "__main__":
    input_json_path = "C:\\_VOIS Work\\Data Analytics Role\\demo-ai-Project-templet\\src\\main\\json_output_input_files\\project_1.json"
    process_rag_output(input_json_path)
