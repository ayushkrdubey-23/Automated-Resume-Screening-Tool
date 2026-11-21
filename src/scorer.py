import math
from collections import Counter


def _tokenize(text):
    """Split cleaned text into tokens (words)."""
    if not text:
        return []
    return text.split()


def _compute_tf(tokens):
    """Term frequency: count of each token divided by total tokens."""
    total = len(tokens)
    if total == 0:
        return {}
    counts = Counter(tokens)
    return {token: count / total for token, count in counts.items()}


def _compute_idf(all_token_lists):
    """Inverse document frequency: log(N / df) for each token."""
    N = len(all_token_lists)
    df = Counter()
    for tokens in all_token_lists:
        unique = set(tokens)
        for token in unique:
            df[token] += 1
    return {token: math.log(N / count) for token, count in df.items()}


def _compute_tfidf_vector(tokens, tf, idf):
    """TF-IDF vector as a dict {token: tfidf_score}."""
    return {token: tf.get(token, 0) * idf.get(token, 0) for token in idf}


def _cosine_similarity(vec1, vec2):
    """Cosine similarity between two dict-based vectors."""
    common = set(vec1.keys()) & set(vec2.keys())
    dot = sum(vec1[t] * vec2[t] for t in common)
    norm1 = math.sqrt(sum(v * v for v in vec1.values()))
    norm2 = math.sqrt(sum(v * v for v in vec2.values()))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)


def score_resumes(resumes_texts, job_description_text):
    """Score each resume against the job description using pure-Python TF-IDF + Cosine Similarity.

    Args:
        resumes_texts: dict {filename: cleaned_text}
        job_description_text: cleaned JD string

    Returns:
        dict {filename: score out of 100}
    """
    if not resumes_texts:
        return {}

    # Tokenize all documents
    all_names = list(resumes_texts.keys())
    all_texts = list(resumes_texts.values()) + [job_description_text]
    all_token_lists = [_tokenize(t) for t in all_texts]

    # Compute IDF across all documents
    idf = _compute_idf(all_token_lists)

    # Compute TF-IDF vector for each resume and for the JD
    resume_tfidfs = []
    for tokens in all_token_lists[:-1]:
        tf = _compute_tf(tokens)
        resume_tfidfs.append(_compute_tfidf_vector(tokens, tf, idf))

    jd_tokens = all_token_lists[-1]
    jd_tf = _compute_tf(jd_tokens)
    jd_tfidf = _compute_tfidf_vector(jd_tokens, jd_tf, idf)

    # Cosine similarity between each resume and the JD
    scores = {}
    for i, name in enumerate(all_names):
        sim = _cosine_similarity(resume_tfidfs[i], jd_tfidf)
        scores[name] = round(sim * 100, 2)

    return scores
