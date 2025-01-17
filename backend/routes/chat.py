from flask import Blueprint, request, jsonify, current_app
from openai_client import get_chat_completion
from config import OPENAI_MODEL, OPENAI_ROLE_SYSTEM_KEY, OPENAI_ROLE_SYSTEM_CONTENT, OPENAI_ROLE_USER_KEY

# Create a Blueprint for the /chat route
chat_blueprint = Blueprint("chat", __name__)

@chat_blueprint.route("/chat", methods=["POST"])
def simple_chat():
    """
    Handle POST requests to the /chat endpoint.

    Returns:
        JSON response with assistant's reply or error message.
    """
    current_app.logger.info("Received a request at /chat")
    try:
        data = request.json
        current_app.logger.info(f"Request data: {data}")

        user_message = data.get("message")
        if not user_message:
            current_app.logger.error("No message found in the request data")
            return jsonify({"error": "Message is required"}), 400

        # Build messages
        messages = [
            {"role": OPENAI_ROLE_SYSTEM_KEY, "content": OPENAI_ROLE_SYSTEM_CONTENT},
            {"role": OPENAI_ROLE_USER_KEY, "content": user_message},
        ]

        # Get assistant reply
        assistant_reply = get_chat_completion(OPENAI_MODEL, messages)
        current_app.logger.info(f"OpenAI response: {assistant_reply}")

        return jsonify({"reply": assistant_reply})

    except Exception as e:
        current_app.logger.error(f"Error during request handling: {e}")
        return jsonify({"error": str(e)}), 500

@chat_blueprint.route("/chat/audio", methods=["POST"])
def chat_with_audio():
    """
    Handle audio-based chat requests to the /chat/audio endpoint.
    """
    current_app.logger.info("Received a request at /chat/audio")
    # Placeholder for audio chat functionality
    return jsonify({"message": "Audio chat functionality not implemented yet"}), 501

@chat_blueprint.route("/chat/image", methods=["POST"])
def chat_image_generator():
    """
    Handle image generation requests to the /chat/image endpoint.
    """
    current_app.logger.info("Received a request at /chat/image")
    # Placeholder for image generation functionality
    return jsonify({"message": "Image generation functionality not implemented yet"}), 501        