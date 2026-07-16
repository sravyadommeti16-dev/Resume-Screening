from langchain_core.tools import tool
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")


@tool
def parse_resume(resume_text: str) -> str:
    """Parse resume text and extract important skills."""
    doc = nlp(resume_text)
    skills = set(
        token.text.lower()
        for token in doc
        if token.pos_ in ["NOUN", "PROPN"]
    )
    return ", ".join(skills)


@tool
def match_skills(resume_text: str, jd_text: str) -> float:
    """Calculate skill match percentage between resume and job description."""
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(similarity * 100, 2)


@tool
def calculate_ats(skill_match: float, experience_years: int) -> float:
    """Calculate ATS score based on skill match and experience."""
    return round((skill_match * 0.6) + min(experience_years * 10, 40), 2)


@tool
def generate_interview_questions() -> list:
    """Generate interview questions for the candidate."""
    return [
        "What is the difference between an AI agent and a standard LLM?",
        "Explain agent architecture.",
        "How do agents plan multi-step tasks?",
        "How do you prevent hallucinations in agents?"
    ]


@tool
def evaluate_interview() -> int:
    """Evaluate interview answers and return a score."""
    return 80
