from google import genai
from config import GEMINI_API_KEY

# Initialize Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)


def chat_with_gemini(prompt):
    """
    Sends a user prompt to Google Gemini and returns the AI response.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",

            contents=[
                "You are a helpful AI assistant. "
                "Keep your responses concise, accurate, and under 150 words unless the user explicitly asks for more detail.",
                prompt,
            ],

            config={
                "temperature": 0.5,
                "max_output_tokens": 200,
            },
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"