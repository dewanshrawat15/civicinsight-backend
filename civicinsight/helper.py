from dotenv import load_dotenv
import os
import google.generativeai as genai
from google.generativeai.types import file_types

load_dotenv()

GEMINI_API_KEY=os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

class GeminiHelper:

    def __init__(self) -> None:
        self.config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=self.config
        )

    def uploadImage(self, image_path):
        mime_type = ""
        file = genai.upload_file(image_path, mime_type=mime_type)
        return file
    
    def structureChat(self, image_path, user_message):
        file = self.uploadImage(image_path=image_path)
        chat_session = self.model.start_chat(
            history=[{
            "role": "user",
            "parts": [ file ],
            }]
        )
        response = chat_session.send_message("The image uploaded highlights several issues, issues common to public infrastructure. Return a key value pair json, where the key tags return a list of public infrastructure issues, isImageFake where this field tells if an image is fake or genuine.")
        return response.text

