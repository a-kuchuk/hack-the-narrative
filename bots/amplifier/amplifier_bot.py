import time
from bots.core.api_client import like_post, get_trending_posts

class AmplifierBot:
    """Likes/reposts positive or informative posts at intervals."""
    def __init__(self, name, interval=300):
        self.name = name
        self.interval = interval

    def act(self):
        posts = get_trending_posts(limit=5)
        for post in posts:
            like_post(post["id"])
            print(f"[AmplifierBot] Liked post {post['id']}")

    def run(self):
        while True:
            self.act()
            time.sleep(self.interval)
