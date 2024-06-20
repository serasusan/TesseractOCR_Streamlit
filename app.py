import streamlit as st
import pytesseract as pt
from PIL import Image
import os

# Specify the path to the Tesseract executable if it's not in your PATH
# Uncomment and set the correct path if needed
# pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

os.environ['TESSDATA_PREFIX'] = r'/usr/share/tesseract-ocr/4.00/tessdata'


st.title("OCR App")
st.write("This is a simple OCR app using Tesseract")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    st.write("Extracting text...")
    text = pt.image_to_string(image,lang='mal+eng')
    st.write(text)
