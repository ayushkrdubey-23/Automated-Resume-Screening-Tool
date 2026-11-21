import csv
import os


def generate_report(resumes_dict, scores, matched_skills_dict,
                    missing_skills_dict, threshold=60,
                    output_path='outputs/screening_report.csv'):
    """Generate a CSV screening report.

    Args:
        resumes_dict: dict {filename: raw_text} (used only for iteration)
        scores: dict {filename: score}
        matched_skills_dict: dict {filename: [skills]}
        missing_skills_dict: dict {filename: [skills]}
        threshold: score above which candidate is shortlisted
        output_path: path to write CSV

    Returns:
        sorted list of (name, score) tuples
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Sort by score descending
    sorted_resumes = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Rank', 'Resume Name', 'Score (%)',
            'Matched Skills', 'Missing Skills', 'Decision'
        ])

        for rank, (name, score) in enumerate(sorted_resumes, start=1):
            matched = ', '.join(matched_skills_dict.get(name, []))
            missing = ', '.join(missing_skills_dict.get(name, []))
            decision = 'Shortlisted' if score >= threshold else 'Rejected'
            writer.writerow([rank, name, score, matched, missing, decision])

    return sorted_resumes
