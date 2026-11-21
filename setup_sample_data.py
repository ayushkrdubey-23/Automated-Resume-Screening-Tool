"""Create sample resumes (TXT) and a job description so you can run the tool immediately."""
import os

RESUME_FOLDER = 'resumes'
DATA_FOLDER = 'data'

os.makedirs(RESUME_FOLDER, exist_ok=True)
os.makedirs(DATA_FOLDER, exist_ok=True)

resumes = {
    'resume_alice.txt': """Alice Johnson
Email: alice@example.com
Experience: Python Developer with 4 years of experience in backend development.
Skills: Python, Django, Flask, SQL, PostgreSQL, REST APIs, Git, Linux, AWS, Docker.
Education: B.Tech Computer Science.
""",
    'resume_bob.txt': """Bob Smith
Email: bob@example.com
Experience: Data Analyst with 3 years experience.
Skills: Python, Pandas, NumPy, SQL, Tableau, Excel, Statistics, Data Analysis.
Education: B.Sc Data Science.
""",
    'resume_carol.txt': """Carol Lee
Email: carol@example.com
Experience: Frontend Developer with 2 years experience.
Skills: JavaScript, React, HTML, CSS, Git, Node.js, Express.
Education: B.Tech Information Technology.
""",
    'resume_david.txt': """David Kim
Email: david@example.com
Experience: Machine Learning Engineer with 5 years experience.
Skills: Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, Scikit-learn,
NLP, AWS, Docker, Kubernetes, SQL.
Education: M.S. Artificial Intelligence.
""",
    'resume_emma.txt': """Emma Wilson
Email: emma@example.com
Experience: HR Executive with 3 years experience.
Skills: Recruitment, Employee Relations, Communication, Leadership, Excel, PowerPoint.
Education: B.B.A Human Resources.
"""
}

for filename, content in resumes.items():
    path = os.path.join(RESUME_FOLDER, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Create a default job description if missing
jd_path = os.path.join(DATA_FOLDER, 'job_description.txt')
if not os.path.exists(jd_path):
    jd_content = """Job Title: Python Developer

Required Skills:
- Python
- SQL
- Git
- Django
- Flask
- REST APIs
- Linux
- AWS
- Docker

Preferred Skills:
- Machine Learning
- Pandas
- Scikit-learn
- Kubernetes

Experience: 2+ years backend development
Education: Bachelor's in Computer Science
"""
    with open(jd_path, 'w', encoding='utf-8') as f:
        f.write(jd_content)

print("Sample data created!")
print(f"Resumes: {RESUME_FOLDER}/")
print(f"Job Description: {jd_path}")
print("Run: python main.py")
