import os
import openai
from dotenv import load_dotenv

load_dotenv()
TEAM_KEY = os.getenv("TEAM_KEY")
MODEL = "gemma3:4b"
ENDPOINT = "http://llm-proxy.legitreal.com/openai"

client = openai.Client(api_key=TEAM_KEY, base_url=ENDPOINT)

def gen_content(prompt: str, system_message: str) -> str:
    if not TEAM_KEY:
        raise ValueError("TEAM_KEY missing in .env")
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
