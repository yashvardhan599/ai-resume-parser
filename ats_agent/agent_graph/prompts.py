RESUME_PARSER_PROMPT = """
Extract structured resume data strictly in JSON.
Fields:
- name
- email
- phone
- total_experience_years
- skills (list)
- education (list)
- companies (list)

Resume:
{resume_text}
"""

JD_MATCH_PROMPT = """
Compare resume JSON with job description and return JSON:
- matched_skills
- missing_skills
- experience_fit (High/Medium/Low)
- domain_fit (High/Medium/Low)

Resume:
{resume}

JD:
{jd}
"""

SCORER_PROMPT = """
Given JD match analysis, produce final score (0-100) and category.
Return JSON:
- final_score
- category
- reasoning

JD Match:
{jd_match}
"""

EXPLANATION_PROMPT = """
Explain why this candidate received the score.

parsed resume:
{parsed_resume}

jd match:
{jd_match}

score:
{score}

Mention strengths, gaps, and interview focus areas.
"""
