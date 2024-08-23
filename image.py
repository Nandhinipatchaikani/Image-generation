import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": "Bearer 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"}

st.title("WELCOME TO EZHIL'S IMAGE GENERATOR")

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": st.text_input("Enter your Imagination : "),
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if st.button("Generate Output"):
	st.image(image)
