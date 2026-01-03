import json
from llm.errors import InvalidLLMOutput

def parse_and_validate(response: str) -> dict:
    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        raise InvalidLLMOutput("Output is not valid JSON")

    if "answer" not in data or "confidence" not in data:
        raise InvalidLLMOutput("Missing required fields")

    return data
