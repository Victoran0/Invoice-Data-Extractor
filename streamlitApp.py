import streamlit as st
from PIL import Image
from get_details import input_invoice_details
from model import get_gemini_response


# Initialize our streamlit app
st.set_page_config(page_title="Invoice Data Extractor")

st.header("Invoice Data Extractor")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader(
    "Choose an invoice:", type=['jpg', 'jpeg', 'png'])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice.", use_column_width=True)

submit = st.button("Tell me about the Invoice")

input_prompt = """
You are an expert in understanding invoices. We will upload an image of invoices and you will have to answer any questions based on the uploaded invoice image.
"""

# If submit button is clicked
if submit:
    image_data = input_invoice_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("RESPONSE:")
    st.write(response)
