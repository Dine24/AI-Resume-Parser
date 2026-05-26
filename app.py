import streamlit as st
from utils.Parser import extract_text_from_pdf
from utils.ats_score import calculate_ats_score
from utils.prompts import generate_summary

st.title("AI Resume Agent")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

jd_text = st.text_area("Paste Job Description")

if uploaded_file and jd_text:

    resume_text = extract_text_from_pdf(uploaded_file)

    ats_score = calculate_ats_score(resume_text, jd_text)

    st.subheader("ATS Match Score")
    st.write(f"{ats_score}%")

    summary = generate_summary(resume_text, jd_text)

    st.subheader("Generated Professional Summary")
    st.write(summary)
