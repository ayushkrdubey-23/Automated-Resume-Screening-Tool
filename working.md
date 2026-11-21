# Project Working Documentation

This document explains how the Automated Resume Screening Tool works, how to execute each file, what each file does, and all files needed in the project.

---

## Project Overview

The Automated Resume Screening Tool is a Python-based NLP system that automates the first stage of candidate screening. It reads resumes (PDF/DOCX/TXT), extracts text, cleans it, matches skills against a job description, computes a similarity score using TF-IDF and Cosine Similarity, ranks candidates, and produces a CSV report with shortlist/reject decisions and explainable skill gaps.

---

## How the Project Works (End-to-End Workflow)

```
Step 1: Resume Upload / Sample Data
       ↓
Step 2: Text Extraction (PDF/DOCX/TXT → plain text)
       ↓
Step 3: Text Cleaning (lowercase, punctuation removal, stopword filtering)
       ↓
Step 4: Skill Matching (keyword matching against skill dictionary)
       ↓
Step 5: Similarity Scoring (TF-IDF + Cosine Similarity vs Job Description)
       ↓
Step 6: Ranking & Shortlist Decision (sort by score, apply threshold)
       ↓
Step 7: Report Generation (CSV with Rank, Score, Matched Skills, Missing Skills, Decision)
```

---

## File-by-File Execution Guide

### Root Level Files

| File | How to Execute | What It Does |
|------|---------------|--------------|
| `main.py` | `python main.py` | Entry point. Runs the full 6-phase screening pipeline: loads JD, extracts resume text, cleans text, matches skills, scores resumes, generates CSV report. Prints ranked table to terminal. |
| `app.py` | `python -m streamlit run app.py` | Streamlit web dashboard. Provides a UI for job description input, real-time single resume upload scoring, batch screening from `resumes/` folder, and CSV download. |
| `setup_sample_data.py` | `python setup_sample_data.py` | Generates 5 sample resumes (TXT) in `resumes/` and a sample job description in `data/job_description.txt`. Run this first if you have no sample data. |
| `requirements.txt` | `pip install -r requirements.txt` | Lists all Python dependencies. Not executed directly; used to install libraries. |
| `README.md` | Open in any text editor / Markdown viewer | Project documentation for GitHub. Overview, features, installation, how to run, sample output, interview prep. |
| `working.md` | Open in any text editor / Markdown viewer | This file. Explains how the project works, file roles, and execution commands. |
| `.gitignore` | Not executed | Tells Git which files/folders to ignore (venv, __pycache__, etc.). |

### `src/` Module Files

| File | How to Execute | What It Does |
|------|---------------|--------------|
| `src/__init__.py` | Not executed directly (imported) | Makes `src` a Python package so modules can be imported. |
| `src/extractor.py` | Imported by `main.py` and `app.py` | Extracts text from PDF (`pdfplumber`), DOCX (`python-docx`), and TXT files. Provides `extract_resume_text()` and `load_all_resumes()`. |
| `src/cleaner.py` | Imported by `main.py` and `app.py` | Cleans raw text: lowercase, removes punctuation, stopwords, and extra whitespace. Provides `clean_text()` and `clean_resumes()`. |
| `src/matcher.py` | Imported by `main.py` and `app.py` | Matches skills from a resume against a skill dictionary using word-boundary regex (avoids false matches like "Java" in "JavaScript"). Provides `extract_skills()` and `get_missing_skills()`. |
| `src/scorer.py` | Imported by `main.py` and `app.py` | Computes TF-IDF vectors and Cosine Similarity between each resume and the job description using pure Python (no `scikit-learn`, to avoid blocked DLLs). Returns scores 0–100. Provides `score_resumes()`. |
| `src/reporter.py` | Imported by `main.py` and `app.py` | Generates the CSV screening report. Sorts candidates by score, applies threshold for shortlist/reject, writes `outputs/screening_report.csv`. Provides `generate_report()`. |

### Data & Resource Files

| File | Location | Purpose |
|------|----------|---------|
| `data/job_description.txt` | `data/` | The job description text file used as the benchmark for matching. Edit this to screen for any role. |
| `resumes/*.txt` | `resumes/` | Sample candidate resumes. Add your own PDF/DOCX/TXT files here for batch screening. |
| `outputs/screening_report.csv` | `outputs/` | Generated report with Rank, Resume Name, Score (%), Matched Skills, Missing Skills, Decision. |

---

## Execution Commands

### Windows PowerShell

```powershell
# 1. Initialize (first time only)
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Create sample data (optional, if you need test data)
python setup_sample_data.py

# 4. Run the CLI pipeline
python main.py

# 5. Run the Streamlit dashboard
python -m streamlit run app.py
```

### Mac / Linux

```bash
# 1. Initialize (first time only)
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Create sample data (optional)
python setup_sample_data.py

# 4. Run the CLI pipeline
python main.py

# 5. Run the Streamlit dashboard
python -m streamlit run app.py
```

---

## What Each File Is Needed For

| File | Needed For |
|------|------------|
| `main.py` | Running the complete screening pipeline from the command line |
| `app.py` | Running the interactive web dashboard (optional, requires Streamlit) |
| `src/extractor.py` | Reading resume text from PDF, DOCX, and TXT files |
| `src/cleaner.py` | Normalizing resume text before matching and scoring |
| `src/matcher.py` | Finding which required skills are present or missing in each resume |
| `src/scorer.py` | Calculating the match score between a resume and the job description |
| `src/reporter.py` | Creating the final CSV report with rankings and decisions |
| `setup_sample_data.py` | Creating sample resumes and a job description for testing |
| `data/job_description.txt` | The job description that resumes are compared against |
| `resumes/` | Folder containing candidate resume files |
| `outputs/` | Folder where the generated CSV report is saved |
| `requirements.txt` | List of Python packages to install |
| `.gitignore` | Files/folders to exclude from Git |

---

## Minimum Files Required to Run

To run the project, you need at minimum:

1. `main.py` — the pipeline entry point
2. `src/__init__.py` — package marker
3. `src/extractor.py` — text extraction
4. `src/cleaner.py` — text cleaning
5. `src/matcher.py` — skill matching
6. `src/scorer.py` — scoring
7. `src/reporter.py` — report generation
8. `data/job_description.txt` — job description input
9. `resumes/*.txt` (or any PDF/DOCX/TXT) — at least one resume
10. `requirements.txt` — to install dependencies

Optional but recommended:
- `app.py` — Streamlit dashboard
- `setup_sample_data.py` — to quickly generate test data
- `README.md` — documentation
- `.gitignore` — for clean Git commits

---

## Output Format (`outputs/screening_report.csv`)

| Column | Description |
|--------|-------------|
| Rank | Position in the sorted list (1 = best match) |
| Resume Name | Filename of the candidate's resume |
| Score (%) | Match score out of 100 (TF-IDF + Cosine Similarity) |
| Matched Skills | Skills from the dictionary found in the resume |
| Missing Skills | Required skills not found in the resume |
| Decision | "Shortlisted" if score ≥ threshold, else "Rejected" |

---

## Notes

- The default shortlist threshold is 60% (configurable in `main.py` and `app.py`).
- Skill matching uses word-boundary regex, so "Java" will not falsely match "JavaScript".
- The scorer uses pure Python TF-IDF + Cosine Similarity (no `scikit-learn`) to avoid system DLL blocking issues.
- PDF support depends on `pdfplumber`; if its compiled extensions are blocked on your system, use TXT or DOCX resumes instead.
- Streamlit's `.exe` may be blocked on some systems; use `python -m streamlit run app.py` instead of `streamlit run app.py`.
