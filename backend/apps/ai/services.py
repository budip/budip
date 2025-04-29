import json
import logging
import base64
import traceback
from PIL import Image
from io import BytesIO
import openai

from django.conf import settings
from .price_finder import fetch_prices_from_stores

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# OpenAI API configuration
openai.api_key = settings.OPENAI_API_KEY

# Simple in-memory history
user_histories = {}


def analyze_uploaded_image(uploaded_file):
    try:
        # Resize and prepare image
        image = Image.open(uploaded_file)
        if image.width > 1024:
            ratio = 1024 / float(image.width)
            new_height = int(image.height * ratio)
            image = image.resize((1024, new_height), Image.LANCZOS)

        buffer = BytesIO()
        image.save(buffer, format="JPEG", quality=85)
        buffer.seek(0)

        base64_image = base64.b64encode(buffer.read()).decode("utf-8")
        image_data_url = f"data:image/jpeg;base64,{base64_image}"

        # Vision prompt
        vision_prompt = (
            "Respond only with a raw JSON object containing the following fields:\n"
            "- 'title': a short, catchy title for the image.\n"
            "- 'caption': a concise one-line caption.\n"
            "- 'alt_text': a clear, descriptive alt text.\n"
            "- 'categories': an array of 2–4 relevant keywords that describe the image.\n"
            "- 'description': 1–3 paragraphs describing the image naturally.\n"
            "- 'search_query': a string that could be used to find this item online for shopping.\n"
            "Respond in strict JSON format without any markdown or triple backticks."
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

        logger.debug(f"Sending to OpenAI Vision API")
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=400
        )

        reply_text = response.choices[0].message.content.strip()
        logger.debug(f"OpenAI raw reply:\n{reply_text}")

        # 🧹 Clean unexpected triple backticks if present
        if reply_text.startswith("```"):
            reply_text = reply_text.lstrip("`").strip()
            if reply_text.lower().startswith("json"):
                reply_text = reply_text[4:].strip()
            reply_text = reply_text.rstrip("`").strip()

        parsed_reply = json.loads(reply_text)

        search_query = parsed_reply.get("search_query")
        categories = parsed_reply.get("categories", [])

        # 🛒 Check if categories are buyable
        buyable_keywords = {
            "Electronics", "Appliances", "Furniture", "Clothing", "Tools",
            "Sports", "Household", "Toys", "Home Decor", "Garden", "Office Supplies"
        }

        # Case insensitive matching
        is_buyable = any(
            category.lower() in (word.lower() for word in buyable_keywords)
            for category in categories
        )

        if search_query and is_buyable:
            logger.debug(f"🛒 Buyable item detected: {search_query}")
            prices = fetch_prices_from_stores(search_query)
            parsed_reply["prices"] = prices
        else:
            logger.info(f"Not a buyable item based on categories {categories}. Skipping price fetch.")

        return parsed_reply

    except Exception as e:
        logger.error(f"❌ Error analyzing uploaded image: {str(e)}")
        traceback.print_exc()
        raise e


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