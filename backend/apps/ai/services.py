import openai
import traceback
import logging
import base64
from django.conf import settings
from PIL import Image
from io import BytesIO

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

openai.api_key = settings.OPENAI_API_KEY

# Simple in-memory history
user_histories = {}

def get_openai_response_image_analyzer(uploaded_file):
    try:
        # 🖼️ Resize to 1024px width if needed
        image = Image.open(uploaded_file)
        if image.width > 1024:
            ratio = 1024 / float(image.width)
            new_height = int(image.height * ratio)
            image = image.resize((1024, new_height), Image.LANCZOS)  # <-- Updated here

        # Convert to JPEG in memory
        buffer = BytesIO()
        image.save(buffer, format="JPEG", quality=85)
        buffer.seek(0)

        # Encode to base64
        base64_image = base64.b64encode(buffer.read()).decode("utf-8")
        image_data_url = f"data:image/jpeg;base64,{base64_image}"

        # Vision prompt
        vision_prompt = (
            "Respond only with a raw JSON object containing the following fields:\n"
            "- 'title': a short, catchy title for the image.\n"
            "- 'caption': a concise one-line caption.\n"
            "- 'alt_text': a clear, descriptive alt text.\n"
            "- 'categories': an array of 2–4 relevant keywords that describe the image "
            "(e.g., ['Space', 'Astronomy', 'Galaxy']).\n"
            "- 'description': 1 to 3 paragraphs that describe what the image is about. "
            "This should be written in natural, engaging language as if describing it for a YouTube video description "
            "or product listing on Shopify. Avoid markdown or formatting.\n"
            "Respond in strict JSON format. Do not include markdown formatting or triple backticks."
        )

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": image_data_url}},
                    {"type": "text", "text": vision_prompt}
                ]
            }
        ]

        logger.debug(f"🧠 Sending image to OpenAI (resized to width ≤ 1024px)")
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=300
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
        if user_id not in user_histories:
            user_histories[user_id] = [{
                "role": "system",
                "content": "You are a helpful assistant. Format all responses in Markdown unless instructed otherwise."
            }]

        user_histories[user_id].append({"role": "user", "content": prompt})
        logger.debug(f"[User {user_id}] Prompt: {prompt}")

        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=user_histories[user_id],
            temperature=0.7,
        )

        logger.debug(f"[User {user_id}] Full response: {response}")

        reply = response.choices[0].message.content.strip()
        user_histories[user_id].append({"role": "assistant", "content": reply})
        return reply

    except Exception as e:
        logger.error(f"[User {user_id}] Error during OpenAI call: {str(e)}")
        traceback.print_exc()
        return "⚠️ Sorry, there was a problem getting a response from the AI."