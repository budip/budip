import yaml
from openai import OpenAI

# Function to load the OpenAI API key from `secrets/open_ai.yml`
def load_api_key():
    with open("secrets/open_ai.yml", "r") as file:
        config = yaml.safe_load(file)
        return config["credentials"]["openai_api_key"]

# Load the API key
api_key = load_api_key()

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Make a request to the OpenAI API
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", 
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Here's the report from national weather system. East to southeast winds 30 to 40 mph with gusts up to 65 mph expected in Central Coast, North Coast, Western Strait of Juan De Fuca, Bellevue and Vicinity, and East Puget Sound Lowlands from 2 PM Tuesday to 4 AM PST Wednesday; damaging winds may cause downed trees, power lines, widespread power outages, and difficult travel conditions, especially for high-profile vehicles. My question, will it has potential to cause problems and outage tonight?"
        }
    ]
)

# Print the result
print(completion.choices[0].message)