import streamlit as st
import os
import sys
import tempfile

# Allow running streamlit from project root
sys.path.insert(0, os.path.dirname(__file__))

from src.extractor import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt
from src.cleaner import clean_text
from src.matcher import extract_skills, get_missing_skills, DEFAULT_SKILLS
from src.scorer import score_resumes
from src.reporter import generate_report
from src.extractor import load_all_resumes

st.set_page_config(page_title="Resume Screening Tool", layout="wide")

st.title("Automated Resume Screening Tool")
st.markdown("Upload resumes, paste a job description, and get ranked candidate scores.")

RESUME_FOLDER = 'resumes'
JD_FILE = 'data/job_description.txt'
OUTPUT_FILE = 'outputs/screening_report.csv'

st.sidebar.header("Settings")
THRESHOLD = st.sidebar.slider("Shortlist Threshold (%)", 0, 100, 60)

st.sidebar.header("Job Description")
jd_input = st.sidebar.text_area(
    "Paste Job Description",
    height=200,
    value="We are hiring a Python Developer with experience in Python, SQL, "
          "machine learning, pandas, scikit-learn, AWS, Docker, and Git."
)

if st.sidebar.button("Save Job Description"):
    os.makedirs('data', exist_ok=True)
    with open(JD_FILE, 'w', encoding='utf-8') as f:
        f.write(jd_input)
    st.sidebar.success("Job description saved!")

# ---------- Real-time single resume upload ----------
st.header("📄 Upload a Resume for Real-Time Scoring")

uploaded_file = st.file_uploader(
    "Choose a resume file (PDF, DOCX, TXT)",
    type=["pdf", "docx", "txt"]
)

def extract_text_from_uploaded(uploaded_file):
    """Extract text from a Streamlit uploaded file object."""
    if uploaded_file is None:
        return ""
    name = uploaded_file.name.lower()
    content = uploaded_file.read()
    # Save to a temp file so extractors can read by path
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(name)[1]) as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    try:
        if name.endswith('.pdf'):
            return extract_text_from_pdf(tmp_path)
        elif name.endswith('.docx'):
            return extract_text_from_docx(tmp_path)
        elif name.endswith('.txt'):
            return extract_text_from_txt(tmp_path)
        else:
            return ""
    finally:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass

if uploaded_file is not None:
    raw_text = extract_text_from_uploaded(uploaded_file)
    if raw_text.strip():
        cleaned_resume = clean_text(raw_text)
        matched = extract_skills(cleaned_resume, DEFAULT_SKILLS)
        missing = get_missing_skills(DEFAULT_SKILLS, matched)

        st.subheader(f"Result for: {uploaded_file.name}")

        if os.path.exists(JD_FILE):
            with open(JD_FILE, 'r', encoding='utf-8', errors='ignore') as f:
                job_description = f.read()
            cleaned_jd = clean_text(job_description)

            # Score this single resume against the JD
            scores = score_resumes({uploaded_file.name: cleaned_resume}, cleaned_jd)
            score = scores.get(uploaded_file.name, 0.0)

            decision = "Shortlisted" if score >= THRESHOLD else "Rejected"
            color = "green" if decision == "Shortlisted" else "red"

            col1, col2, col3 = st.columns(3)
            col1.metric("Score", f"{score}%")
            col2.metric("Decision", decision)
            col3.metric("Threshold", f"{THRESHOLD}%")

            st.markdown(f"**Decision:** :{color}[{decision}]")

            st.write("**Matched Skills:**", ", ".join(matched) if matched else "None")
            st.write("**Missing Skills:**", ", ".join(missing) if missing else "None")
        else:
            st.warning("Job description not found. Please save it in the sidebar first.")
            st.write("**Matched Skills:**", ", ".join(matched) if matched else "None")
            st.write("**Missing Skills:**", ", ".join(missing) if missing else "None")
    else:
        st.error("Could not extract text from the uploaded file.")

st.markdown("---")

# ---------- Batch screening from resumes folder ----------
st.sidebar.header("Batch Screening")
st.sidebar.write(f"Place resume files (PDF/DOCX/TXT) in: `{RESUME_FOLDER}/`")

if st.sidebar.button("Run Batch Screening"):
    if not os.path.exists(JD_FILE):
        st.error("Job description not found. Please save it first.")
    else:
        with open(JD_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            job_description = f.read()

        raw_resumes = load_all_resumes(RESUME_FOLDER)
        if not raw_resumes:
            st.error(f"No resumes found in {RESUME_FOLDER}")
        else:
            from src.cleaner import clean_resumes
            cleaned_resumes = clean_resumes(raw_resumes)
            cleaned_jd = clean_text(job_description)

            matched = {}
            missing = {}
            for name, text in cleaned_resumes.items():
                found = extract_skills(text, DEFAULT_SKILLS)
                matched[name] = found
                missing[name] = get_missing_skills(DEFAULT_SKILLS, found)

            scores = score_resumes(cleaned_resumes, cleaned_jd)
            sorted_resumes = generate_report(
                raw_resumes, scores, matched, missing,
                threshold=THRESHOLD, output_path=OUTPUT_FILE
            )

            st.success(f"Batch screening complete! Report saved to {OUTPUT_FILE}")

            st.subheader("Ranked Candidates")
            for rank, (name, score) in enumerate(sorted_resumes, start=1):
                decision = "Shortlisted" if score >= THRESHOLD else "Rejected"
                color = "green" if decision == "Shortlisted" else "red"
                st.markdown(
                    f"**{rank}. {name}** — Score: {score}% — "
                    f":{color}[{decision}]"
                )
                with st.expander(f"Details for {name}"):
                    st.write("Matched Skills:", ", ".join(matched.get(name, [])) or "None")
                    st.write("Missing Skills:", ", ".join(missing.get(name, [])) or "None")

            st.subheader("Download Report")
            with open(OUTPUT_FILE, 'rb') as f:
                st.download_button(
                    label="Download CSV Report",
                    data=f,
                    file_name="screening_report.csv",
                    mime="text/csv"
                )
