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
    st.write(f"### Overall Resume Match: {match_score}%")
    
    # Skill gap analysis
    result = skill_gap_analysis(jd_text, resume_text)

    # Display results in two columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Matched Skills")
        if result["matched"]:
            for skill in result["matched"]:
                st.success(skill)
        else:
            st.write("No matched skills found.")

    with col2:
        st.subheader("Missing Skills")
        if result["missing"]:
            for skill in result["missing"]:
                st.error(skill)
        else:
            st.write("✅ No skill gaps found!")