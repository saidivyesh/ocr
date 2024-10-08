import streamlit as st
from PIL import Image
import pytesseract
import re

# Step 1: Function to extract text using OCR for both Hindi and English
def extract_text(image):
    extracted_text = pytesseract.image_to_string(image, lang='hin+eng')
    return extracted_text

# Step 2: Function to search and highlight the keyword in the extracted text
def search_keyword(extracted_text, keyword):
    if keyword.lower() in extracted_text.lower():
        # Highlight the keyword in the text using re for case-insensitive replacement
        highlighted_text = re.sub(f"(?i)({re.escape(keyword)})", r"[\1]", extracted_text)
        return highlighted_text
    else:
        return f"Keyword '{keyword}' not found. Here is the extracted text:\n\n{extracted_text}"

# Streamlit Interface
st.title("Hindi and English OCR App")

# Step 1: Upload Image
uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Convert the uploaded file to a PIL image
    image = Image.open(uploaded_image)
    
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Extract text from the image
    extracted_text = extract_text(image)
    
    # Display the extracted text
    st.subheader("Extracted Text")
    st.text_area("Extracted Text", value=extracted_text, height=200)
    
    # Step 2: Enter keyword for search
    keyword = st.text_input("Enter Keyword to Search")

    if keyword:
        # Perform keyword search and highlight
        highlighted_text = search_keyword(extracted_text, keyword)
        
        # Display the highlighted result
        st.subheader("Search Result")
        st.text_area("Highlighted Text", value=highlighted_text, height=200)
