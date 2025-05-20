from common.imports import *


class VertexAI:
    def __init__(self, project: str, location: str):
        """Initialize VertexAI object with project id and location

        Args:
            project (str): _description_
            location (str): _description_
        """
        self.project = project
        self.location = location
        self._initialize()

    def _initialize(self):
        """Internal method to initialize VertexAI SDK"""
        vertexai.init(project=self.project, location=self.location)
