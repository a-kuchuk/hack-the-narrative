import time
from bots.core.api_client import post_status, get_trending_tags
from bots.core.ai_client import gen_content

class InfluencerBot:
    """Posts positive, engaging, and informative content periodically."""
    def __init__(self, name, interval=3600):
        self.name = name
        self.interval = interval

    def act(self):
        trending = get_trending_tags()
        system_msg = (
            "You are a friendly influencer bot. Create engaging posts that are informative, "
            "positive, and support your candidate or community initiatives."
        )
        prompt = f"Create a short post for {self.name} including trending topics: {trending}"
        content = gen_content(prompt, system_msg)
        post_status(content)
        print(f"[InfluencerBot] Posted: {content}")

    def run(self):
        while True:
            self.act()
            time.sleep(self.interval)
