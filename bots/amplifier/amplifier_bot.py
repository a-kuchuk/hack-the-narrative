import time
from bots.core.api_client import like_post, get_trending_posts
from bots.core.ai_client import gen_content

class AmplifierBot:
    """Likes/reposts positive or neutral posts supporting Victor Hawthorne."""

    SUPPORTED_KEYWORDS = [
    # Name & Identity
    "Victor Hawthorne",

    # Policies / Promises
    "Free college",
    "Job training",
    "Progressive taxes",
    "Carbon taxes",
    "Ban on offshore drilling",
    "Police reform",
    "Military reform",
    "Community investment",
    "Dismantling “oligarchic” power structures",

    # Style / Persona
    "Passionate",
    "Relentless",
    "Voice for the people",
    "Community-focused",
    "Progressive",

    # Neutral / Community Topics
    "Kingston",
    "Community",
    "Progress",
    "Local news"
]
    def __init__(self, name, interval=300):
        self.name = name
        self.interval = interval

    def is_supported_or_neutral(self, post_content: str) -> bool:
        """
        Simple check to see if a post is either neutral or supportive.
        Returns True if any supported keyword appears.
        """
        content_lower = post_content.lower()
        return any(k.lower() in content_lower for k in self.SUPPORTED_KEYWORDS)

    def act(self):
        posts = get_trending_posts(limit=10)
        for post in posts:
            if self.is_supported_or_neutral(post["content"]):
                like_post(post["id"])
                print(f"[AmplifierBot] Liked post {post['id']}: {post['content']}")

    def run(self):
        while True:
            self.act()
            time.sleep(self.interval)
