import string

# Built-in English stopwords (no external download required)
STOP_WORDS = {
    'a', 'an', 'the', 'and', 'or', 'but', 'if', 'then', 'else', 'when',
    'at', 'from', 'by', 'for', 'with', 'about', 'against', 'between',
    'into', 'through', 'during', 'before', 'after', 'above', 'below',
    'to', 'of', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
    'further', 'once', 'here', 'there', 'when', 'where', 'why', 'how',
    'all', 'each', 'few', 'more', 'most', 'other', 'some', 'such',
    'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
    'very', 'can', 'will', 'just', 'should', 'now', 'is', 'are', 'was',
    'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do',
    'does', 'did', 'doing', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours',
    'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he',
    'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
    'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what',
    'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am'
}


def clean_text(text):
    """Clean raw resume text: lowercase, remove punctuation, stopwords, extra spaces."""
    if not text:
        return ""

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove extra whitespace / newlines
    text = ' '.join(text.split())

    # Remove stopwords
    words = text.split()
    words = [w for w in words if w not in STOP_WORDS]

    return ' '.join(words)


def clean_resumes(resumes_dict):
    """Clean all resumes in a dictionary.

    Returns a dict: {filename: cleaned_text}
    """
    return {name: clean_text(text) for name, text in resumes_dict.items()}
