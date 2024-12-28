import os
from pathlib import Path

import google.generativeai as genai
import PIL.Image
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY_GOOGLE"))


# Path to image
image_path = Path("input/test_lecture_note_photo.jpg")

sample_file = PIL.Image.open(image_path)

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-exp-1206")

prompt = "The photograph shows some lecture notes. Please transcribe the text in this photograph to markdown, using latex for equations where needed."

response = model.generate_content([prompt, sample_file])

print(response.text)

open(Path("output/output_example_gemini.md"), "w").write(response.text)
