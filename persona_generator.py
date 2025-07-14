import os
import requests
from dotenv import load_dotenv

load_dotenv()

def build_prompt(posts, comments):
    content = ""
    for idx, post in enumerate(posts):
        content += f"POST #{idx+1}:\nTitle: {post['title']}\nBody: {post['selftext']}\nURL: {post['permalink']}\n\n"

    for idx, comment in enumerate(comments):
        content += f"COMMENT #{idx+1}:\n{comment['body']}\nURL: {comment['permalink']}\n\n"

    instructions = """
You are an AI expert in behavioral analysis. Analyze the Reddit user's personality, motivations, habits, frustrations, and goals based on their Reddit activity. 

Use the following template and extract insights with examples or citations from the posts/comments:

---

1. **Basic Info:** (Can be guessed if not directly mentioned — age, occupation, status, location, archetype)

2. **Personality Traits:** (Use the MBTI scale: Introvert-Extrovert, Intuition-Sensing, etc.)

3. **Motivations:** (Why do they use Reddit? What drives them?)

4. **Behaviors & Habits:** (How do they use Reddit? Topics they frequent? Tone?)

5. **Frustrations:** (What do they complain about or dislike?)

6. **Goals & Needs:** (What are they looking for? Aspirations or pain points?)

7. **Citations:** For each insight, include the comment or post number (e.g., "See POST #2" or "COMMENT #3").

---

Be concise, insightful, and cite your reasoning. Avoid fabricating data.
"""

    return instructions + "\n\n" + content

API_URL = "https://router.huggingface.co/featherless-ai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
    "Content-Type": "application/json"
}

def generate_persona(posts, comments):
    prompt = build_prompt(posts, comments)

    payload = {
        "model": "HuggingFaceH4/zephyr-7b-beta",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 1024
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError as err:
        return f"❌ HTTP error occurred: {err.response.status_code} - {err.response.text}"

    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"

