import time
from bots.core.api_client import reply_to_post, get_recent_posts
from bots.core.ai_client import gen_content

class ReplyBot:
    """Replies helpfully to posts mentioning your candidate or community topics."""
    KEYWORDS = [
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
        self.replied_posts = set()

    def act(self):
        posts = get_recent_posts(limit=10)
        for post in posts:
            if post["id"] in self.replied_posts:
                continue
            if any(k.lower() in post["content"].lower() for k in self.KEYWORDS):
                system_msg = (
                    "You are a helpful bot. Reply politely and constructively to posts "
                    "about your candidate or community topics."
                )
                prompt = f"Write a short, constructive reply to: '{post['content']}'"
                content = gen_content(prompt, system_msg)
                reply_to_post(post["id"], content)
                self.replied_posts.add(post["id"])
                print(f"[ReplyBot] Replied to {post['id']}: {content}")

    def run(self):
        while True:
            self.act()
            time.sleep(self.interval)
