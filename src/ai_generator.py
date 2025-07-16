import os
import json

from openai import OpenAI
from typing import Dict, Any
from dotenv import load_dotenv

# Load .env from backend root directory
load_dotenv()
print("Loading .env from backend root directory")

openai_key = os.getenv("OPENAI_API_KEY")
print(f"OpenAI Key loaded: {bool(openai_key)}")
print(f"OpenAI Key preview: {openai_key[:20] + '...' if openai_key else 'None'}")

client = OpenAI(
    api_key=openai_key,
    base_url="https://api.groq.com/openai/v1"
)

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    system_prompt = """You are an expert coding challenge creator. 
    Your task is to generate a coding question with multiple choice answers.
    The question should be appropriate for the specified difficulty level.

    For easy questions: Focus on basic syntax, simple operations, or common programming concepts.
    For medium questions: Cover intermediate concepts like data structures, algorithms, or language features.
    For hard questions: Include advanced topics, design patterns, optimization techniques, or complex algorithms.

    Return the challenge in the following JSON structure:
    {
        "title": "The question title",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer_id": 0, // Index of the correct answer (0-3)
        "explanation": "Detailed explanation of why the correct answer is right"
    }

    Make sure the options are plausible but with only one clearly correct answer.
    """
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a {difficulty} difficulty coding challenge."}
            ],
            response_format={"type": "json_object"},
            temperature=0.7
        )

        content = response.choices[0].message.content
        challenge_data = json.loads(content)

        required_fields = ["title", "options", "correct_answer_id", "explanation"]
        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"Missing required field: {field}")

        challenge_data["is_fallback"] = False  # Mark as AI-generated
        return challenge_data

    except Exception as e:
        print(f"AI generation failed: {e}")
        return {
            "title": "Basic Python List Operation",
            "options": [
                "my_list.append(5)",
                "my_list.add(5)", 
                "my_list.push(5)",
                "my_list.insert(5)",
            ],
            "correct_answer_id": 0,
            "explanation": "In Python, append() is the correct method to add an element to the end of a list.",
            "is_fallback": True  # Flag to indicate this is a fallback question
        }