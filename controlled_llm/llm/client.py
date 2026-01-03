# llm/client.py

def call_llm(prompt: str) -> str:
    """
    Simulates a raw LLM API call.
    No validation. No parsing.
    """
    if "bad" in prompt:
        return "I think the answer is 42"
    
    return """
    {
        "answer": "42",
        "confidence": 0.9
    }
    """
