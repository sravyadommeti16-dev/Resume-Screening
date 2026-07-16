from tools import match_skills, calculate_ats, evaluate_interview

with open("resume.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()

with open("job_description.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

experience_years = 3

skill_match = match_skills.invoke({
    "resume_text": resume_text,
    "jd_text": jd_text
})

ats_score = calculate_ats.invoke({
    "skill_match": skill_match,
    "experience_years": experience_years
})

interview_score = evaluate_interview.invoke({})

final_score = round((ats_score + interview_score) / 2, 2)
decision = "SHORTLISTED" if final_score >= 75 else "REJECTED"

print("\n===== AGENTIC AI FINAL DECISION =====")
print(f"Skill Match: {skill_match}%")
print(f"ATS Score: {ats_score}")
print(f"Interview Score: {interview_score}")
print(f"Final Score: {final_score}")
print(f"Decision: {decision}")
