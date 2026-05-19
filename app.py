import streamlit as st
import os

from src.parser import extract_text
from src.preprocess import clean_text
from src.matcher import match_resumes

st.title("AI Resume Screening System")

job_description = st.text_area("Enter Job Description")

if st.button("Screen Resumes"):

    resume_folder = "data/resumes"

    resume_texts = []
    resume_names = []

    for file in os.listdir(resume_folder):

        file_path = os.path.join(resume_folder, file)

        text = extract_text(file_path)

        cleaned = clean_text(text)

        resume_texts.append(cleaned)

        resume_names.append(file)

    cleaned_jd = clean_text(job_description)

    scores = match_resumes(cleaned_jd, resume_texts)

    results = list(zip(resume_names, scores))

    results = sorted(results, key=lambda x: x[1], reverse=True)

    st.subheader("Ranking Results")

    for rank, (name, score) in enumerate(results, start=1):

        st.write(f"{rank}. {name} - Match Score: {round(score*100,2)}%")
        
