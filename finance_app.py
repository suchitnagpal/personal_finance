<<<<<<< HEAD
import streamlit as st
import fitz  # PyMuPDF
from together_client import summarize_statement

st.set_page_config(page_title="Finance Consultant", layout="wide")
st.title("💰 Personal Finance Consultant")

st.write("Upload your bank or credit-card statement (PDF), and I'll summarize your spending.")

uploaded_pdf = st.file_uploader("Choose a PDF file", type=["pdf"])
if uploaded_pdf is not None:
    with st.spinner("Extracting text from PDF…"):
        # read the uploaded file bytes
        pdf_bytes = uploaded_pdf.read()
        # open PDF from bytes
        pdf = fitz.open(stream=pdf_bytes, filetype="pdf")
        all_text = ""
        for page in pdf:
            all_text += page.get_text() + "\n"
        pdf.close()

    st.success("PDF text extracted. Consulting your personal expert...")
    with st.spinner("Summarizing statement…"):
        summary = summarize_statement(all_text)

    st.subheader("Statement Summary")
    st.write(summary)
=======
import streamlit as st
import fitz  # PyMuPDF
from together_client import summarize_statement

st.set_page_config(page_title="Finance Consultant", layout="wide")
st.title("💰 Personal Finance Consultant")

st.write("Upload your bank or credit-card statement (PDF), and I'll summarize your spending.")

uploaded_pdf = st.file_uploader("Choose a PDF file", type=["pdf"])
if uploaded_pdf is not None:
    with st.spinner("Extracting text from PDF…"):
        # read the uploaded file bytes
        pdf_bytes = uploaded_pdf.read()
        # open PDF from bytes
        pdf = fitz.open(stream=pdf_bytes, filetype="pdf")
        all_text = ""
        for page in pdf:
            all_text += page.get_text() + "\n"
        pdf.close()

    st.success("PDF text extracted. Consulting your personal expert...")
    with st.spinner("Summarizing statement…"):
        summary = summarize_statement(all_text)

    st.subheader("Statement Summary")
    st.write(summary)
>>>>>>> 4a8de3e3a9ae6372e8f996f07de9e7ad579ad7e7
