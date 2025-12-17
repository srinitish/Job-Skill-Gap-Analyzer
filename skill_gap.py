import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_from_pdf(path):
    text =''
    reader = PyPDF2.PdfReader(path)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text+=page_text
    return text


SKILLS = [
    "python", "java", "sql", "machine learning",
    "data science", "deep learning", "nlp",
    "tensorflow", "pandas", "numpy",
    "git", "docker", "aws","python", "java", "sql", "c", "c++", "c#", "javascript", "typescript",
    "php", "ruby", "go", "rust", "html", "css","react", "angular", "vue", "next.js", "django", "flask", "spring", "express", "node.js",
    "aws", "azure", "google cloud", "gcp", "heroku",
    "docker", "kubernetes", "terraform", "git",
    "penetration testing", "ethical hacking", "network security",
    "firewall", "cryptography", "incident response",
    "figma", "adobe xd", "sketch", "wireframing", "prototyping", "user research",
    "excel", "tableau", "power bi", "hadoop", "spark", "big data",
    "data visualization", "statistics",
    "linux", "bash", "shell scripting", "jira", "agile", "scrum"
]


def extract_skill_from_jd(jd_text):
    jd_text = jd_text.lower()
    return [skill for skill in SKILLS if skill in jd_text]

def extract_skill_from_resume(resume_text, jd_skills):
    resume_text = resume_text.lower()
    return [skill for skill in jd_skills if skill in resume_text]

def skill_similarity(jd_text, resume_text):
    jd_skills = extract_skill_from_jd(jd_text)
    resume_skills = extract_skill_from_resume(resume_text, jd_skills)
     
    jd_str = " ".join(jd_skills)
    resume_str = " ".join(resume_skills)

    if not jd_str or not resume_str:
        return 0.0
    
    tfidf = TfidfVectorizer()
    vector = tfidf.fit_transform([jd_str, resume_str])
    score = cosine_similarity(vector[0:1], vector[1:2])[0][0]
    
    return round(score * 100, 2)

def skill_gap_analysis(jd_text,resume_text):
    jd_skills = extract_skill_from_jd(jd_text)
    resume_skills = extract_skill_from_resume(resume_text, jd_skills)
    missing = list(set(jd_skills)-set(resume_skills))
    return missing
