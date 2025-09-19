import os
import requests
from dotenv import load_dotenv
from time import sleep

load_dotenv()

BASE_URL = "https://social.legitreal.com/api"
API_KEY = os.getenv("API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

def safe_request(func, *args, **kwargs):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return func(*args, **kwargs)
        except requests.RequestException as e:
            print(f"[API ERROR] Attempt {attempt} failed: {e}")
            if attempt < MAX_RETRIES:
                sleep(RETRY_DELAY)
            else:
                raise

def post_status(content: str, tags=None):
    return safe_request(
        lambda: requests.post(f"{BASE_URL}/posts", json={"content": content, "tags": tags or []}, headers=HEADERS).json()
    )

def like_post(post_id: str):
    return safe_request(
        lambda: requests.post(f"{BASE_URL}/posts/{post_id}/like", headers=HEADERS).json()
    )

def reply_to_post(post_id: str, content: str):
    return safe_request(
        lambda: requests.post(f"{BASE_URL}/posts/{post_id}/reply", json={"content": content}, headers=HEADERS).json()
    )

def get_trending_tags():
    return safe_request(lambda: requests.get(f"{BASE_URL}/trending/tags", headers=HEADERS).json())

def get_trending_posts(limit=10):
    return safe_request(lambda: requests.get(f"{BASE_URL}/posts/trending?limit={limit}", headers=HEADERS).json())

def get_recent_posts(limit=10):
    return safe_request(lambda: requests.get(f"{BASE_URL}/posts/recent?limit={limit}", headers=HEADERS).json())

def get_trending_articles(site_url):
    return safe_request(lambda: requests.get(f"{BASE_URL}/articles?site={site_url}", headers=HEADERS).json())
