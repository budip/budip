from openai import OpenAI
from config import load_api_key

# Initialize the OpenAI client
api_key = load_api_key()
client = OpenAI(api_key=api_key)

def get_chat_completion(model, messages):
    """
    Wrapper for OpenAI chat completions.
    """
    try:
        completion = client.chat.completions.create(model=model, messages=messages)
        return completion.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"Error communicating with OpenAI API: {e}")