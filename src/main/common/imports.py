from google.cloud import aiplatform
from google.cloud.aiplatform import gapic as aiplatform_gapic
import vertexai
from vertexai.generative_models import GenerativeModel, Part  # part is for file upload
import os
import json
import sys
