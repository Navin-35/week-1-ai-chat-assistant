from google import genai
from config import GEMINI_API_KEY

# Initialize Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)


def chat_with_gemini(prompt):
    """
    Send a prompt to Google Gemini and return the response.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"