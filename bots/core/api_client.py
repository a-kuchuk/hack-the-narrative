import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://social.legitreal.com/api"
API_KEY = os.getenv("API_KEY")

def post_status(content: str, tags=None):
    print(f"[API Stub] Would POST: {content} #{tags or []}")
    return {"id": "dummy_post_id"}

def like_post(post_id: str):
    print(f"[API Stub] Would LIKE post {post_id}")
    return {"id": post_id}

def reply_to_post(post_id: str, content: str):
    print(f"[API Stub] Would REPLY to {post_id}: {content}")
    return {"id": f"{post_id}_reply"}

def get_trending_tags():
    print("[API Stub] Would fetch trending tags")
    return [{"name": "Kingston"}, {"name": "KingstonForward"}]
