import time


def generate_openai_prompt(prompt: str) -> str:
    """
    Simple client for OpenAi Api request
    """
    # with requests.Session() as session:
    #         },

    time.sleep(10)
    return f"The answer is: {random.randint(0, 50)}"
