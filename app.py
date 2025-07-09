import streamlit as st
from utils.extract_skills import extract_text_from_pdf, clean_text
from utils.match_score import calculate_similarity

st.set_page_config(page_title="Resume Matcher", layout="centered")

st.title("📄 Resume & Job Matcher")
st.markdown("Upload your **resume** and paste the **job description** to check match score.")

resume = st.file_uploader("Upload Resume (PDF only)", type="pdf")
job_description = st.text_area("Paste Job Description here", height=200)

if st.button("Match Now") and resume and job_description:
    raw_resume = extract_text_from_pdf(resume)
    resume_clean = clean_text(raw_resume)
    jd_clean = clean_text(job_description)

    score = calculate_similarity(resume_clean, jd_clean)
    st.success(f"✅ Match Score: **{score}%**")

    if score >= 70:
        st.info("🟢 Great match! You're likely a strong candidate.")
    elif score >= 40:
        st.warning("🟡 Moderate match. Consider tailoring your resume.")
    else:
        st.error("🔴 Low match. You may need to update your skills.")
