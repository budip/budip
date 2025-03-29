import openai
import traceback
import logging
import base64
from django.conf import settings

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

openai.api_key = settings.OPENAI_API_KEY

# Simple in-memory history
user_histories = {}

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_openai_response_image_analyzer(uploaded_file):
    try:
        # 🔁 Read and encode the uploaded image
        base64_image = base64.b64encode(uploaded_file.read()).decode("utf-8")
        mime_type = uploaded_file.content_type or "image/jpeg"
        image_data_url = f"data:{mime_type};base64,{base64_image}"

        # 🧠 Prompt to generate caption, title, alt-text
        vision_prompt = "Respond only with a raw JSON object containing 'title', 'caption', and 'alt_text'. Do not include markdown formatting or triple backticks."

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": image_data_url}},
                    {"type": "text", "text": vision_prompt}
                ]
            }
        ]

        logger.debug(f"🧠 Sending image to OpenAI (mime: {mime_type})")
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=300,
        )

        reply = response.choices[0].message.content.strip()
        logger.debug(f"✅ OpenAI Vision response:\n{reply}")
        return reply

    except Exception as e:
        logger.error(f"❌ Error in image analyzer: {str(e)}")
        traceback.print_exc()
        return "⚠️ Error analyzing the image."
    

def get_openai_response(prompt, user_id=1):
    try:
        # Initialize history if needed
        if user_id not in user_histories:
            user_histories[user_id] = [{"role": "system", "content": "You are a helpful assistant."}]

        # Append new user prompt
        user_histories[user_id].append({"role": "user", "content": prompt})
        logger.debug(f"[User {user_id}] Prompt: {prompt}")

        # Make OpenAI API call
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=user_histories[user_id],
            temperature=0.7,
        )

        # Inspect full response (for debugging structure)
        logger.debug(f"[User {user_id}] Full response: {response}")

        # Extract reply content safely
        reply = response.choices[0].message.content.strip()
        user_histories[user_id].append({"role": "assistant", "content": reply})
        return reply

    except Exception as e:
        logger.error(f"[User {user_id}] Error during OpenAI call: {str(e)}")
        traceback.print_exc()
        return "⚠️ Sorry, there was a problem getting a response from the AI."