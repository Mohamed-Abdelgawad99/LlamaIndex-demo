from common.imports import *
from model_runner.initvertexai import VertexAI
from model_runner.user_input import UserInput
from model_runner.system_instrcutions import SYSTEM_INSTRUCTIONS
from model_runner.model import ModelHandler
from rag_output_handler import json_processor
from rag_output_handler import json_saver


class Main:
    def __init__(
        self,
        project: str,
        location: str,
        model_version: str,
        old_json_file_path: dict,
    ):
        """
        Initializ Vertex AI and set up the model version

        Args:
            project (str): Name of you GCP project
            location (str): GCP Project Location
            model_version (str): The GenAI model you are using from Vertex AI Model Garden
            json_file_path (dict): The pre-processed JSON data
        """
        # Preprocessing the json file output from the rag phase
        processor = json_processor.JsonProcessor(old_json_file_path)
        processor.load_json()
        processor.process_usecases()
        updated_data = processor.get_proessed_data()
        self.new_json_file_path = json_saver.JsonSaver.save_json(
            updated_data, old_json_file_path
        )
        print(f"New Json file path is -> {self.new_json_file_path}")
        # loading the data in the new json file to pass to the model
        with open(self.new_json_file_path, "r") as file:
            self.json_data = json.load(file)
        # Instantiatin the model from VertexAI Model Garden
        VertexAI(project, location)
        self.model_version = model_version

    def run(self):
        """
        Main Entry point. Fetcing the System Istructions (chatbot persona) and
        Interact with the model
        """
        system_instruction_options = ["Java", "Python", "Robot", "Cypress"]
        user_input_instance = UserInput(system_instruction_options)
        user_input_instance.display_options()
        language_choice = user_input_instance.get_user_choice()
        bot_persona = SYSTEM_INSTRUCTIONS.get(language_choice)

        # Initialize an instance of the Model Handler class with the system instructions
        model_handler = ModelHandler(self.model_version, bot_persona, self.json_data)

        model_handler.handle_request()


if __name__ == "__main__":
    PROJECTID = "intricate-shard-445011-j8"
    LOCATION = "us-central1"
    MODEL_VERSION = "gemini-1.5-pro"
    OLD_JSON_FILEPATH = "C:\\_VOIS Work\\Data Analytics Role\\demo-ai-Project-templet\\src\\main\\json_output_input_files\\project_1.json"

    tobi_sdet = Main(PROJECTID, LOCATION, MODEL_VERSION, OLD_JSON_FILEPATH)
    tobi_sdet.run()
