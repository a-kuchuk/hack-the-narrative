import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://social.legitreal.com/api"
API_KEY = os.getenv("API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def post_status(content: str, tags=None):
    """Create a new post."""
    data = {"content": content, "tags": tags or []}
    response = requests.post(f"{BASE_URL}/posts", json=data, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def like_post(post_id: str):
    """Like an existing post."""
    response = requests.post(f"{BASE_URL}/posts/{post_id}/like", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def reply_to_post(post_id: str, content: str):
    """Reply to an existing post."""
    data = {"content": content}
    response = requests.post(f"{BASE_URL}/posts/{post_id}/reply", json=data, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_trending_tags():
    """Fetch trending tags."""
    response = requests.get(f"{BASE_URL}/trending/tags", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_trending_posts(limit=10):
    """Fetch trending posts for filtering/amplifying."""
    response = requests.get(f"{BASE_URL}/posts/trending?limit={limit}", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_recent_posts(limit=10):
    """Fetch recent posts for ReplyBot."""
    response = requests.get(f"{BASE_URL}/posts/recent?limit={limit}", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_trending_articles(site_url):
    """Fetch trending articles from a given site."""
    response = requests.get(f"{BASE_URL}/articles?site={site_url}", headers=HEADERS)
    response.raise_for_status()
    return response.json()
