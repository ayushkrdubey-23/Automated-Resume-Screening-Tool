import os
from src.extractor import load_all_resumes
from src.cleaner import clean_text, clean_resumes
from src.matcher import extract_skills, get_missing_skills, DEFAULT_SKILLS
from src.scorer import score_resumes
from src.reporter import generate_report

# Configuration
RESUME_FOLDER = 'resumes'
JD_FILE = 'data/job_description.txt'
OUTPUT_FILE = 'outputs/screening_report.csv'
THRESHOLD = 60  # Score >= 60 => Shortlisted


def main():
    print("=" * 60)
    print("Automated Resume Screening Tool")
    print("=" * 60)

    # 1. Load Job Description
    if not os.path.exists(JD_FILE):
        print(f"[ERROR] Job description not found: {JD_FILE}")
        return

    with open(JD_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        job_description = f.read()

    print(f"\n[1/6] Loaded Job Description from {JD_FILE}")

    # 2. Load and extract resumes
    raw_resumes = load_all_resumes(RESUME_FOLDER)
    if not raw_resumes:
        print(f"[ERROR] No resumes found in {RESUME_FOLDER}")
        return
    print(f"[2/6] Extracted text from {len(raw_resumes)} resume(s)")

    # 3. Clean text
    cleaned_resumes = clean_resumes(raw_resumes)
    cleaned_jd = clean_text(job_description)
    print("[3/6] Cleaned all resumes and job description")

    # 4. Skill matching
    matched_skills_dict = {}
    missing_skills_dict = {}
    for name, text in cleaned_resumes.items():
        found = extract_skills(text, DEFAULT_SKILLS)
        matched_skills_dict[name] = found
        missing_skills_dict[name] = get_missing_skills(DEFAULT_SKILLS, found)
    print("[4/6] Matched skills against default skill dictionary")

    # 5. Score resumes using TF-IDF + Cosine Similarity
    scores = score_resumes(cleaned_resumes, cleaned_jd)
    print("[5/6] Calculated similarity scores")

    # 6. Generate report
    sorted_resumes = generate_report(
        raw_resumes, scores, matched_skills_dict,
        missing_skills_dict, threshold=THRESHOLD,
        output_path=OUTPUT_FILE
    )

    print(f"[6/6] Report saved to {OUTPUT_FILE}\n")

    # Print summary to terminal
    print("-" * 60)
    print(f"{'Rank':<6}{'Resume':<25}{'Score':<8}{'Decision'}")
    print("-" * 60)
    for rank, (name, score) in enumerate(sorted_resumes, start=1):
        decision = 'Shortlisted' if score >= THRESHOLD else 'Rejected'
        print(f"{rank:<6}{name:<25}{score:<8}{decision}")
    print("-" * 60)
    print(f"Threshold: {THRESHOLD}%")
    print("Done! Open outputs/screening_report.csv for full details.")


if __name__ == '__main__':
    main()
