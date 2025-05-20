from common.imports import *


class ModelHandler:
    def __init__(self, model_version: str, system_isntruction: str, json_data: dict):
        """Initialize the model with its version and system instructions

        Args:
            model_version (str): GenAI model from VertexAI model garden
            system_isntruction (str): ChatBot Persona
            json_data (dict): The pre-processed JSON data
        """
        self.model = GenerativeModel(
            model_version, system_instruction=system_isntruction
        )
        self.conversation_history = []
        self.json_data = json_data

    def generate_prompt_for_usecases(self, usecase_name, usecase_details):
        """Generating prompts for the bot using the project description and usecase details from the json file"""
        prompt = f"Description: {self.json_data.get('description', '')}\n"
        prompt += f"Usecase Name: {usecase_name}\n"
        prompt += f"Status: {usecase_details.get('status')}\n"
        prompt += f"Coverage Scope: {usecase_details.get('coverage_scope', 'not available')}\n"

        files = usecase_details.get("files", {})
        if files:
            prompt += "Files:\n"
            for file_name, file_content in files.items():
                prompt += (
                    f" - {file_name}: {file_content.get('path', 'not available')}\n"
                )
                content = file_content.get("contents")
                incomplete_parts = file_content.get("incomplete_parts")
                if content:
                    prompt += f"   Contents: {content}\n"
                if incomplete_parts:
                    prompt += f"   Incomplete Parts: {incomplete_parts}\n"
        return prompt

    def handle_request(self):
        """Manage API interactions between user and remote model"""
        print("Sending relevant repo info and usecases to the model....\n")
        # Remove description from the json_data (or handle it separately if needed)
        usecases_data = {k: v for k, v in self.json_data.items() if k != "description"}
        for usecase_name, usecase_details in usecases_data.items():
            prompt = self.generate_prompt_for_usecases(usecase_name, usecase_details)
            # print(f"Generated Prompt for {usecase_name}: {prompt}")  # Debugging line
            # append the user's input to the conversation histroy
            self.conversation_history.append(
                {"role": "user", "parts": [{"text": prompt}]}
            )
            # pass the conversation history to the model
            response = self.model.generate_content(
                contents=self.conversation_history, stream=False
            )
            # adding the model response to the conversation history
            self.conversation_history.append(
                {"role": "model", "parts": [{"text": response.text}]}
            )
            print(f"Model Response for {usecase_name}:\n")
            print(response.text)
            print("-" * 80)


"""------------------------------- Function for chatting ---------------------------------"""
# def handle_request(self):
#     """Manage API interactions between user and remote model"""
#     print("Type 'exit' to end the conversation.\n")
#     while True:
#         user_prompt = input("You: ")
#         print()
#         if user_prompt.lower() == "exit":
#             print("Exiting Model Conversation")
#             break
#         # append the user's input to the conversation histroy
#         self.conversation_history.append(
#             {"role": "user", "parts": [{"text": user_prompt}]}
#         )
#         # pass the conversation history to the model
#         response = self.model.generate_content(
#             contents=self.conversation_history, stream=False
#         )
#         # adding the model response to the conversation history
#         self.conversation_history.append(
#             {"role": "model", "parts": [{"text": response.text}]}
#         )
#         print(response.text)
