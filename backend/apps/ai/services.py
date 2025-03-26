import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

# Simple in-memory history
user_histories = {}

def get_openai_response(prompt, user_id=1):
    # Initialize history for this user if it doesn't exist
    if user_id not in user_histories:
        user_histories[user_id] = [{"role": "system", "content": "You are a helpful assistant."}]
    
    # Append the new user input
    user_histories[user_id].append({"role": "user", "content": prompt})

    # Get response
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=user_histories[user_id],
        temperature=0.7,
    )

    reply = response.choices[0].message.content

    # Save the assistant's response to history
    user_histories[user_id].append({"role": "assistant", "content": reply})

    return reply