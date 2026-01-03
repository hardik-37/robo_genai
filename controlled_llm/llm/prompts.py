# llm/prompts.py

SYSTEM_INSTRUCTION = """
You are a controlled assistant.
Return ONLY valid JSON with keys: answer, confidence.
Rules:
- Output must be valid JSON.
- Required keys: answer, confidence.
"""

def build_prompt(user_input: str) -> str:
    return f"""
SYSTEM:
{SYSTEM_INSTRUCTION}

USER:
{user_input}
"""
