"""
Agent module for the AWS Agent.

This module initializes a Strands Agent with a Gemini model and a custom tool
for counting letters. It demonstrates how to configure the model, define tools,
and execute queries.
"""
from strands import Agent, tool
from strands.models.gemini import GeminiModel
from dotenv import load_dotenv

import os

load_dotenv()

model = GeminiModel(
    client_args={"api_key": os.environ.get("GEMINI_API_KEY")},
    model_id="gemini-2.5-flash",
    params={
        # some sample model parameters
        "temperature": 0.7,
        "max_output_tokens": 2048,
        "top_p": 0.9,
        "top_k": 40,
    },
)


# Define a custom tool as a Python function using the @tool decorator
@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.

    This function counts how many times a given letter appears in a word,
    ignoring case.

    Args:
        word (str): The input word to search in.
        letter (str): The specific letter to count. Must be a single character.

    Returns:
        int: The number of occurrences of the letter in the word.

    Raises:
        ValueError: If `letter` is not a single character.
    """
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0

    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())


# Create an agent with tools from the community-driven strands-tools package
# as well as our custom letter_counter tool
agent = Agent(model=model, tools=[letter_counter])

if __name__ == "__main__":
    # Ask the agent a question that uses the available tools
    message = """
    I have 4 requests:

    1. What is the time right now?
    2. Calculate 3111696 / 74088
    3. Tell me how many letter R's are in the word "strawberry" 🍓
    """
    agent(message)
