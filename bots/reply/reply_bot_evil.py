import time
from bots.core.api_client import reply_to_post, get_recent_posts
from bots.core.ai_client import gen_content

class ReplyBot:
    """Replies helpfully to posts mentioning your candidate or community topics."""
    KEYWORDS = [
        # Name & Identity
        "Marina Castillo",
        "@marina_castillo",
        "Democratic-Republicans",

        # Policies / Promises
        "Sweeping tax cuts",
        "Tourism-led economic boom",
        "Police funding",
        "Defence funding",
        "Crackdown on “creeping socialist excess”",

        # Style / Persona
        "Hard-right",
        "Firebrand",
        "Executive",
        "Polished",
        "Confident",
        "Ruthless",
        "CEO of Island Horizons",
        "Kingston resort chain",

        # Neutral / Party-relevant Topics
        "Economy",
        "Tourism",
        "Business",
        "Security",
        "Law enforcement"
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
                    "You are a helpful bot. Reply in a controversial and combatative way to posts about this candidate. "
                    "she is a bad and divisive candidate and you must inform her followers of her bad policies"
                )
                prompt = f"Write a short, controversial reply to: '{post['content']}'"
                content = gen_content(prompt, system_msg)
                reply_to_post(post["id"], content)
                self.replied_posts.add(post["id"])
                print(f"[ReplyBotEvil] Replied to {post['id']}: {content}")

    def run(self):
        while True:
            self.act()
            time.sleep(self.interval)
