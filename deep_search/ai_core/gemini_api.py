import google.generativeai as genai
from django.conf import settings
import os

class GeminiAPI:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('GOOGLE_API_KEY') or settings.GOOGLE_API_KEY
        genai.configure(api_key=self.api_key)

        self.generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        self.safety_setting = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            generation_config=self.generation_config,
            safety_settings=self.safety_settings
        )
    
    def get_response(self, prompt):
        try:
            response = self.model.generate_content(promt)

            return response.text
        except Exception as e:
            print(f"Errod calling Gemini API: {e}")
            return None
