## Resume Matcher NLP App

A Streamlit app that compares a resume PDF with a job description and calculates a **match score** using Natural Language Processing (NLP).

## Features

- Upload a PDF resume
- Paste any job description
- Get a real-time match score using cosine similarity
- Built using TF-IDF Vectorization
- Simple UI powered by Streamlit

## Tech Stack

- **Python**
- **Streamlit**
- **PyPDF2** – PDF parsing
- **scikit-learn** – TF-IDF and Cosine Similarity
- **pandas**
- **Regular Expressions**

## How to Run the Project

# 1. Clone the repository
git clone https://github.com/suryaprathapreddyg/resume-matcher-nlp.git
cd resume-matcher-nlp

# 2. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate   # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
