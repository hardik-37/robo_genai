from llm.client import call_llm
from llm.parser import parse_and_validate
from llm.errors import InvalidLLMOutput
from llm.prompts import build_prompt
from llm.logger import logger
from config import MAX_RETRIES



def run(user_input: str):
    prompt = build_prompt(user_input)
    logger.info("Prompt built")

    for attempt in range(1, MAX_RETRIES + 2):
        try:
            logger.info(f"Attempt {attempt}")
            response = call_llm(user_input)
            logger.info(f"Raw response: {response}")

            parsed = parse_and_validate(response)
            logger.info("Output validated successfully")
            print("✅ Final output:", parsed)
            return

        except InvalidLLMOutput as e:
            logger.error(f"Validation failed: {e}")

    raise RuntimeError("LLM failed after retries")


if __name__ == "__main__":
    run("give me a bad answer")
