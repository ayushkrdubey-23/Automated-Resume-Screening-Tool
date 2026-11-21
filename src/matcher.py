import re

# Default skill dictionary. Edit this list to match your target job role.
DEFAULT_SKILLS = [
    'python', 'java', 'javascript', 'c++', 'c#', 'sql', 'mysql', 'postgresql',
    'mongodb', 'machine learning', 'deep learning', 'data analysis', 'data science',
    'pandas', 'numpy', 'scikit-learn', 'tensorflow', 'pytorch', 'keras',
    'natural language processing', 'nlp', 'computer vision', 'statistics',
    'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'git', 'github', 'jenkins',
    'html', 'css', 'react', 'angular', 'vue', 'django', 'flask', 'fastapi',
    'node.js', 'express', 'excel', 'power bi', 'tableau', 'powerpoint',
    'communication', 'leadership', 'project management', 'agile', 'scrum',
    'problem solving', 'teamwork', 'time management'
]


def extract_skills(text, skill_list=None):
    """Find which skills from skill_list appear in the text.

    Uses word-boundary regex so 'java' does not match 'javascript'.
    Returns a list of matched skills.
    """
    if skill_list is None:
        skill_list = DEFAULT_SKILLS

    if not text:
        return []

    text_lower = text.lower()
    found_skills = []

    for skill in skill_list:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return found_skills


def get_missing_skills(required_skills, found_skills):
    """Return skills from required_skills that are not in found_skills."""
    found_set = set(s.lower() for s in found_skills)
    return [s for s in required_skills if s.lower() not in found_set]
