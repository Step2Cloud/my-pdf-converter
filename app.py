import streamlit as st
from pdf2docx import Converter
import os
import tempfile

# Page config
st.set_page_config(page_title="PDF to Word", page_icon="📄")

st.title(" PDF to Word Converter")
st.info("Upload a PDF and I'll convert it to an editable Word document.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    if st.button("Convert to Word"):
        with st.spinner("Converting... this may take a moment."):
            # 1. Create a temporary file to save the upload
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
                tmp_pdf.write(uploaded_file.getvalue())
                tmp_pdf_path = tmp_pdf.name
            
            # 2. Define output path
            docx_path = tmp_pdf_path.replace(".pdf", ".docx")

            try:
                # 3. Perform conversion
                cv = Converter(tmp_pdf_path)
                cv.convert(docx_path)
                cv.close()

                # 4. Read the result and offer download
                with open(docx_path, "rb") as f:
                    st.success("Conversion successful!")
                    st.download_button(
                        label="Download Word Document",
                        data=f,
                        file_name=uploaded_file.name.replace(".pdf", ".docx"),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                # 5. Cleanup temporary files from the server
                if os.path.exists(tmp_pdf_path):
                    os.remove(tmp_pdf_path)
                if os.path.exists(docx_path):
                    os.remove(docx_path)
