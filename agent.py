from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

from tools import (
    parse_resume,
    match_skills,
    calculate_ats,
    generate_interview_questions,
    evaluate_interview
)

# LLM model
model = ChatOllama(
    model="llama3.2",
    temperature=0
)

# Tools list
tools = [
    parse_resume,
    match_skills,
    calculate_ats,
    generate_interview_questions,
    evaluate_interview
]

# ✅ CORRECT: model must be positional
agent = create_react_agent(
    model,
    tools
)
