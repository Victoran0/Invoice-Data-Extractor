import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

GEMINI_API_KEY = os.environ['GEMINI_API_KEY']

genai.configure(api_key=GEMINI_API_KEY)

# Function to load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")


def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text
