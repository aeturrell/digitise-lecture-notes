import base64
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY_OPENAI"))


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
image_path = Path("input/test_lecture_note_photo.jpg")

# Getting the base64 string
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model="chatgpt-4o-latest",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "The photograph shows some lecture notes. Please transcribe the text in this photograph to markdown, using latex for equations where needed.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)

print(response.choices[0])

print(response.choices[0].message.content)

open(Path("output/output_example_gpto.md"), "w").write(
    response.choices[0].message.content
)
