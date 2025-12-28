from skills import ALIASES

def skill_present(skill, text):
    if skill in text:
        return True
    for alias in ALIASES.get(skill, []):
        if alias in text:
            return True
    return False

def analyze_resume(resume_text, job_skills):
    matched = []
    missing = []

    for skill in job_skills:
        if skill_present(skill, resume_text):
            matched.append(skill)
        else:
            missing.append(skill)

    total_weight = sum(job_skills.values())
    matched_weight = sum(job_skills[s] for s in matched)

    score = round((matched_weight / total_weight) * 100, 2)

    high, medium, low = [], [], []

    for skill in missing:
        weight = job_skills[skill]
        if weight >= 3:
            high.append(skill)
        elif weight == 2:
            medium.append(skill)
        else:
            low.append(skill)

    return score, matched, high, medium, low
