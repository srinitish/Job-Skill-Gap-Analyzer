import streamlit as st
from skill_gap import extract_from_pdf, skill_similarity, skill_gap_analysis

st.title("Resume vs Job Description Matcher")

# Upload resume
resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description")

if resume_file and jd_text:
    resume_text = extract_from_pdf(resume_file)
    
    # Match percentage
    match_score = skill_similarity(jd_text, resume_text)
    st.write(f"###Overall Resume Match: {match_score}%")
    
    # Skill gap
    missing_skills = skill_gap_analysis(jd_text, resume_text)
    if missing_skills:
        st.write("### Missing Skills:")
        st.write(", ".join(missing_skills))
    else:
        st.write("✅ No skill gaps found!")