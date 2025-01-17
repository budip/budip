import os
from dotenv import load_dotenv
import yaml

# Load environment variables
load_dotenv()

def get_env_variable(key):
    """
    Retrieve an environment variable or raise an exception if it's missing.
    """
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Missing required environment variable: {key}")
    return value

# Configuration constants
OPENAI_API_KEY_PATH = get_env_variable("OPENAI_CONFIG_PATH")
OPENAI_MODEL = get_env_variable("OPENAI_MODEL")
OPENAI_ROLE_SYSTEM_KEY = get_env_variable("OPENAI_ROLE_SYSTEM_KEY")
OPENAI_ROLE_SYSTEM_CONTENT = get_env_variable("OPENAI_ROLE_SYSTEM")
OPENAI_ROLE_USER_KEY = get_env_variable("OPENAI_ROLE_USER_KEY")

def load_api_key():
    """
    Load the OpenAI API key from the configuration file.
    """
    if not os.path.isfile(OPENAI_API_KEY_PATH):
        raise FileNotFoundError(f"Config file not found: {OPENAI_API_KEY_PATH}")

    with open(OPENAI_API_KEY_PATH, "r") as file:
        return yaml.safe_load(file)["credentials"]["openai_api_key"]