# AI-Based Resume Screening System

## Description
An AI-powered Resume Screening System that automatically ranks resumes based on job description similarity using NLP and Machine Learning techniques.

## Features
- Resume Parsing
- Resume Ranking
- NLP Preprocessing
- TF-IDF Vectorization
- Cosine Similarity Matching
- Streamlit Web Interface

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- NLTK
- PDFPlumber

## Project Workflow
1. Upload resumes
2. Enter job description
3. Text preprocessing
4. Feature extraction using TF-IDF
5. Cosine similarity calculation
6. Resume ranking based on similarity score

## Folder Structure

AI_Resume_Screening_Project/
│
├── data/
│ └── resumes/
│
├── src/
│ ├── parser.py
│ ├── preprocess.py
│ └── matcher.py
│
├── app.py
├── requirements.txt
├── README.md

## Run Project

```bash
streamlit run app.py