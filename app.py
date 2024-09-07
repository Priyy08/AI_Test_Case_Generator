import os
import torch
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import streamlit as st
from io import BytesIO
from groq import Groq

# Initialize BLIP Processor and Model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

# Initialize Groq client
client = Groq(
    api_key='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',
)

def generate_caption_and_tests(image, context=None, product_type="digital"):
    raw_image = Image.open(image).convert('RGB')

    # Conditional image captioning tailored for digital products
    text = "This is a screenshot of a website or app."
    inputs = processor(raw_image, text, return_tensors="pt")

    out = model.generate(**inputs)
    res = processor.decode(out[0], skip_special_tokens=True)

    # Refine product type for websites or apps in the context
    if product_type == "website":
        product_test_query = f"Write 3 test cases for testing the functionality, responsiveness, and UX of a website resembling {res}."
    elif product_type == "app":
        product_test_query = f"Generate 3 test cases to test a mobile app resembling {res}, including functional and usability tests."
    else:
        product_test_query = f"Write 3 generic test cases for {res}."

    if context:
        product_test_query += f" Context: {context}"

    # Query Groq API for test cases based on the caption
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": product_test_query
            }
        ],
        model="llama3-70b-8192",
    )

    # Extract the test cases from the response
    test_cases = chat_completion.choices[0].message.content.strip()

    return res, test_cases

# Streamlit app UI
st.title("Digital Product Testing Instructions Generator")

st.write("Optional: Provide additional context for the test case generation (e.g., describe key features).")
context = st.text_area("Context (optional)", "")

# Select digital product type
product_type = st.selectbox("Select the type of digital product", ["website", "app", "other"])

# Image upload widget
uploaded_file = st.file_uploader("Upload an image (e.g., screenshot of a website/app)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Describe Testing Instructions"):
        with st.spinner("Generating description and test cases..."):
            # Generate image caption and test cases
            description, test_cases = generate_caption_and_tests(uploaded_file, context, product_type)

        # Display results
        st.subheader("Image Description")
        st.write(description)

        st.subheader("Testing Instructions")
        
        # Display test cases with correct formatting
        st.markdown(test_cases.replace("\n", "\n\n"))
