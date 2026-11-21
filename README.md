# Automated Resume Screening Tool

An NLP-based Python application that automates the initial stage of resume screening by extracting candidate information, identifying technical skills, comparing resumes with job descriptions, calculating matching scores, ranking candidates, and generating screening reports.

---

## Project Overview

The **Automated Resume Screening Tool** is a Python-based Natural Language Processing (NLP) project designed to simplify the initial recruitment and candidate screening process.

Recruiters often receive hundreds of resumes for a single job opening. Manually reviewing every resume requires significant time and effort.

This project addresses that challenge by automatically analyzing candidate resumes and comparing them against a given job description.

The system extracts resume text from TXT, PDF, and DOCX documents, performs text cleaning, identifies relevant skills, calculates similarity scores using TF-IDF and Cosine Similarity, ranks candidates, and generates a CSV report containing shortlisted candidates and missing skill information.

The project uses sample resumes and synthetic candidate data to simulate a real-world recruitment screening environment without requiring access to any company's internal Applicant Tracking System (ATS).

## Project Objective

The primary objectives are:

- Automate the initial resume screening process.
- Extract text from PDF, DOCX, and TXT resumes.
- Identify technical skills from candidate resumes.
- Compare candidate profiles with job descriptions.
- Calculate resume matching scores using NLP techniques.
- Identify matched and missing required skills.
- Rank candidates based on their matching scores.
- Generate shortlisted and rejected candidate reports.
- Provide an interactive dashboard for resume screening.
- Demonstrate practical applications of Python, NLP, automation, and text similarity techniques.

## Project Development & Guidance

This project was developed as part of my Python learning and practical project development journey under the guidance of **Mr. Umesh Yadav Sir, Founder of IIP (in collaboration with eDC, IIT Delhi).**

His guidance and mentorship helped me understand practical Python development, project structuring, automation, and the application of technical concepts to real-world problems.

I sincerely thank **Mr. Umesh Yadav Sir** for his valuable guidance and support throughout the project development.

---

## Key Features

### 1. Resume Text Extraction
- Supports TXT resume files.
- Supports PDF resume extraction using `pdfplumber`.
- Supports DOCX resume extraction using `python-docx`.
- Converts document content into processable text.

### 2. Text Cleaning
- Converts text into lowercase.
- Removes unnecessary punctuation.
- Removes stopwords.
- Eliminates extra whitespace.
- Prepares resume content for further analysis.

### 3. Skill Extraction
- Identifies technical skills using a predefined skill dictionary.
- Uses regular expressions for accurate keyword matching.
- Avoids false matches such as matching `Java` inside `JavaScript`.
- Identifies missing skills against job requirements.

### 4. Resume Similarity Analysis
- Uses TF-IDF (Term Frequency-Inverse Document Frequency).
- Applies Cosine Similarity to compare resumes with job descriptions.
- Converts similarity results into percentage-based scores.

### 5. Candidate Ranking
- Ranks candidates according to their matching scores.
- Assigns candidate positions.
- Identifies shortlisted and rejected candidates using a configurable threshold.

### 6. Explainable Screening Results
- Displays matched skills.
- Displays missing skills.
- Shows individual candidate scores.
- Provides ranking and screening decisions.

### 7. CSV Report Generation
- Generates a structured screening report.
- Saves results in `outputs/screening_report.csv`.
- Makes candidate comparisons easier for recruiters.

### 8. Interactive Dashboard
- Provides a Streamlit-based user interface.
- Supports job description input.
- Allows individual resume uploads.
- Supports batch screening from the resumes folder.
- Provides CSV report downloads.

---

## Technology Stack

| Technology | Application |
|---|---|
| Python | Core programming language |
| Pandas | Data handling and report generation |
| NumPy | Numerical computing |
| Regex | Skill and keyword extraction |
| pdfplumber | PDF text extraction |
| python-docx | DOCX text extraction |
| TF-IDF | Text vectorization |
| Cosine Similarity | Resume-job description similarity |
| Streamlit | Interactive dashboard |
| CSV | Screening report storage |
| Git & GitHub | Version control and project hosting |
| VS Code | Development environment |

**Implementation note:** The current scoring module implements TF-IDF and Cosine Similarity using pure Python rather than Scikit-learn. This avoids certain compiled-library compatibility issues in the development environment.

---

## Project Architecture

```text
              RECRUITER
                  |
                  v
          RESUME SCREENING TOOL
                  |
          +-------+--------+
          |                |
          v                v
      RESUMES         JOB DESCRIPTION
          |                |
          v                |
     TEXT EXTRACTION        |
          |                |
          v                |
      TEXT CLEANING         |
          |                |
          +--------+-------+
                   |
                   v
             SKILL MATCHING
                   |
                   v
           TF-IDF VECTORIZATION
                   |
                   v
            COSINE SIMILARITY
                   |
                   v
             SCORE CALCULATION
                   |
                   v
            CANDIDATE RANKING
                   |
                   v
           SHORTLIST DECISION
                   |
                   v
             CSV REPORT
```

## How the Project Works

The project follows a seven-step screening workflow.

### Step 1: Resume Input

The system accepts candidate resumes in TXT, PDF, and DOCX formats.

Sample resumes are stored in the `resumes/` directory.

### Step 2: Text Extraction

The extractor module reads the uploaded resume and extracts its textual content.

Supported formats:

- PDF
- DOCX
- TXT

### Step 3: Text Cleaning

The cleaner module preprocesses the extracted text by converting it into lowercase, removing punctuation, filtering stopwords, and eliminating unnecessary whitespace.

### Step 4: Skill Matching

The matcher module compares resume content against a predefined skill dictionary.

It identifies:

- Matched skills
- Missing skills

Regular expressions with word boundaries help improve keyword matching accuracy.

### Step 5: Similarity Scoring

The scorer module calculates the similarity between the resume and job description.

It uses:

**TF-IDF:** Assigns numerical importance to words based on their frequency and distribution.

**Cosine Similarity:** Measures the similarity between the numerical text representations.

The final similarity score is represented as a percentage between 0 and 100.

### Step 6: Candidate Ranking and Decision

Candidates are sorted according to their matching scores.

The default shortlist threshold is 60%.

- Score greater than or equal to 60%: Shortlisted.
- Score below 60%: Rejected.

The threshold can be configured in the application.

### Step 7: Report Generation

The reporter module generates a CSV report containing:

- Candidate rank
- Resume name
- Matching score
- Matched skills
- Missing skills
- Screening decision

The generated report is saved in the `outputs/` directory.

---

## Project Folder Structure

The following structure represents the current project organization.

```text
Automated-Resume-Screening-Tool/
│
├── data/
│   └── job_description.txt
│
├── outputs/
│   └── screening_report.csv
│
├── resumes/
│   ├── resume_alice.txt
│   ├── resume_bob.txt
│   ├── resume_carol.txt
│   ├── resume_david.txt
│   └── resume_emma.txt
│
├── src/
│   ├── __init__.py
│   ├── cleaner.py
│   ├── extractor.py
│   ├── matcher.py
│   ├── reporter.py
│   └── scorer.py
│
├── venv/
│
├── .gitignore
├── app.py
├── main.py
├── README.md
├── requirements.txt
└── setup_sample_data.py
```

### Folder Description

| Folder | Purpose |
|---|---|
| `data/` | Contains job description and other input data. |
| `outputs/` | Stores generated screening reports. |
| `resumes/` | Contains candidate resumes for screening. |
| `src/` | Contains modular Python implementation files. |
| `venv/` | Contains the project's Python virtual environment. |

### File-by-File Explanation

#### Root-Level Files

| File | Execution | Purpose |
|---|---|---|
| `main.py` | `python main.py` | Executes the complete resume screening pipeline from the terminal. |
| `app.py` | `python -m streamlit run app.py` | Launches the interactive Streamlit dashboard. |
| `setup_sample_data.py` | `python setup_sample_data.py` | Generates five sample resumes and a sample job description. |
| `requirements.txt` | `pip install -r requirements.txt` | Contains the required Python dependencies. |
| `README.md` | Markdown viewer | Provides project documentation. |
| `.gitignore` | Not executed | Prevents unnecessary files from being tracked by Git. |

#### `src/` Module Files

| File | Purpose |
|---|---|
| `__init__.py` | Makes the `src` directory a Python package. |
| `extractor.py` | Extracts text from PDF, DOCX, and TXT resumes. |
| `cleaner.py` | Cleans and preprocesses extracted resume text. |
| `matcher.py` | Identifies matched and missing skills using keyword matching. |
| `scorer.py` | Calculates resume similarity using pure Python TF-IDF and Cosine Similarity. |
| `reporter.py` | Ranks candidates, applies the shortlist threshold, and generates CSV reports. |

#### Data and Resource Files

| File | Purpose |
|---|---|
| `data/job_description.txt` | Contains the job description used as the screening benchmark. |
| `resumes/resume_alice.txt` | Sample resume of candidate Alice. |
| `resumes/resume_bob.txt` | Sample resume of candidate Bob. |
| `resumes/resume_carol.txt` | Sample resume of candidate Carol. |
| `resumes/resume_david.txt` | Sample resume of candidate David. |
| `resumes/resume_emma.txt` | Sample resume of candidate Emma. |
| `outputs/screening_report.csv` | Stores candidate rankings, matching scores, skills, and decisions. |

**Note:** The `venv/` directory and `src/__pycache__/` are local/generated directories and should not be uploaded to GitHub.

---

## Installation and Setup

### Prerequisites

- Python 3.10 or above.
- Visual Studio Code.
- Git.
- Basic knowledge of Python.

### 1. Clone the Repository

```bash
git clone https://github.com/ayushkrdubey-23/-Automated-Resume-Screening-Tool.git
```

```bash
cd Automated-Resume-Screening-Tool
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

### Option 1: Generate Sample Data

If you want to create the sample resumes and job description again, execute:

```bash
python setup_sample_data.py
```

This generates five sample candidate resumes and a job description.

**Note:** Running this script again may overwrite the existing sample files.

### Option 2: Run the Command-Line Application

Execute:

```bash
python main.py
```

The application will:

1. Read the job description.
2. Load available candidate resumes.
3. Extract resume text.
4. Clean extracted text.
5. Identify matched and missing skills.
6. Calculate similarity scores.
7. Rank candidates.
8. Generate the screening report.

### Option 3: Run the Streamlit Dashboard

Execute:

```bash
python -m streamlit run app.py
```

Streamlit will start a local web server and provide a URL, generally:

```text
http://localhost:8501
```

Open the URL in your browser to access the interactive resume screening dashboard.

The dashboard supports job description input, individual resume screening, batch processing, and CSV report downloads.

---

## Sample Screening Report

The system generates:

`outputs/screening_report.csv`

| Column | Description |
|---|---|
| Rank | Candidate's position based on matching score. |
| Resume Name | Candidate resume filename. |
| Score (%) | Similarity score between resume and job description. |
| Matched Skills | Required skills identified in the resume. |
| Missing Skills | Required skills not identified in the resume. |
| Decision | Shortlisted or Rejected based on the configured threshold. |

### Illustrative Output

The following table demonstrates the expected report format. These values are illustrative, not measured execution results.

| Rank | Candidate | Score | Decision |
|---:|---|---:|---|
| 1 | Alice | 88% | Shortlisted |
| 2 | Bob | 76% | Shortlisted |
| 3 | Carol | 64% | Shortlisted |
| 4 | David | 52% | Rejected |
| 5 | Emma | 38% | Rejected |

**Shortlisting threshold:** 60%

Actual scores and rankings depend on the resume content and job description.

---

## Project Execution Commands

| Command | Description |
|---|---|
| `python setup_sample_data.py` | Generate sample resumes and job description. |
| `python main.py` | Run the complete screening pipeline. |
| `python -m streamlit run app.py` | Launch the interactive dashboard. |
| `pip install -r requirements.txt` | Install project dependencies. |
| `git status` | Check repository changes. |
| `git add .` | Stage project files. |
| `git commit -m "message"` | Commit changes. |
| `git push` | Upload commits to GitHub. |

---

## Important Implementation Notes

1. The default shortlist threshold is 60%.
2. Skill matching uses word-boundary regular expressions to reduce incorrect keyword matches.
3. The scoring module uses a pure Python TF-IDF and Cosine Similarity implementation.
4. The project supports PDF, DOCX, and TXT resume extraction.
5. PDF extraction depends on `pdfplumber`.
6. If PDF extraction fails because of an environment compatibility issue, TXT or DOCX files can be used for testing.
7. The system relies on a predefined skill dictionary and is not a complete semantic understanding system.
8. A high similarity score does not guarantee that a candidate is suitable for a job.
9. Screening decisions should be reviewed by a human recruiter before any hiring decision.

---

## Applications and Industry Relevance

The project demonstrates concepts used in modern recruitment technology and Applicant Tracking Systems (ATS).

Potential applications include:

- Initial resume screening.
- Candidate-job description matching.
- Technical skill identification.
- Candidate ranking and comparison.
- Recruitment workflow automation.
- HR analytics and reporting.
- Resume information processing.

It demonstrates practical skills relevant to:

- Python Developer
- Data Analyst
- Machine Learning Engineer
- NLP Engineer
- Automation Developer
- HR Technology Developer

---

## Current Project Limitations

- Skill extraction depends on a predefined keyword dictionary.
- TF-IDF primarily captures textual and keyword similarity.
- The system does not independently verify a candidate's actual experience or qualifications.
- Image-based and scanned resumes may require OCR support.
- The scoring method does not establish candidate suitability or hiring success.
- Sample data is used instead of real company recruitment data.
- The current implementation is a Python CLI and Streamlit application, not an integration with an external ATS.

---

## Future Enhancements

The project can be extended with the following features:

1. **FastAPI Backend:** Expose resume extraction, scoring, and ranking through REST APIs.
2. **Next.js Recruiter Dashboard:** Develop a modern recruitment interface with candidate analytics.
3. **Advanced NLP:** Integrate Sentence Transformers or BERT for semantic resume matching.
4. **Named Entity Recognition:** Extract candidate names, education, experience, and organizations.
5. **Advanced Skill Extraction:** Use NLP-based skill identification instead of relying only on predefined keywords.
6. **Database Integration:** Store candidate profiles, job descriptions, and screening history.
7. **Batch Resume Upload:** Support bulk PDF and DOCX uploads.
8. **Explainable Ranking:** Show how individual matching factors contribute to the final score.
9. **OCR Support:** Extract text from scanned resumes.
10. **Fairness and Bias Auditing:** Evaluate screening outcomes to identify potential discriminatory patterns.
11. **Advanced Reporting:** Generate downloadable PDF and Excel reports.

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and modular application development.
- File handling and document text extraction.
- Regular expressions and text preprocessing.
- Natural Language Processing fundamentals.
- TF-IDF vectorization.
- Cosine Similarity.
- Keyword and skill matching.
- Candidate ranking and scoring.
- CSV report generation using Python.
- Streamlit dashboard development.
- Virtual environment management.
- Git and GitHub version control.
- Building practical automation solutions.

---


## Repository Information

**Repository Name:** `Automated-Resume-Screening-Tool`

**Suggested GitHub Description:**

A Python-based NLP resume screening application that extracts candidate information, matches skills with job descriptions using TF-IDF and Cosine Similarity, ranks candidates, identifies skill gaps, and generates automated screening reports with an interactive Streamlit dashboard.

**GitHub Topics:**

`python` `resume-screening` `nlp` `machine-learning` `tf-idf` `cosine-similarity` `streamlit` `automation` `hr-tech` `candidate-ranking` `text-processing`

---

## Acknowledgement

I would like to express my sincere gratitude to **Mr. Umesh Yadav Sir, Founder of IIP in collaboration with eDC, IIT Delhi**, for his valuable guidance, mentorship, and encouragement throughout my project development journey.

His guidance helped me strengthen my practical programming knowledge and understand how Python concepts can be applied to solve real-world problems.

I am grateful for this learning opportunity and look forward to applying these skills in more advanced projects.

---

## Author

**Ayush**

B.Tech Student | Python Developer | Aspiring Data Scientist and Machine Learning Engineer

GitHub: https://github.com/ayushkrdubey-23/

---

## License

This project is developed for educational purposes, practical learning, and portfolio demonstration.

---

**If you find this project useful, consider giving the repository a star!**
