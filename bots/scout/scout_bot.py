from bots.core.api_client import get_trending_tags

class ScoutBot:
    def __init__(self, name):
        self.name = name

    def act(self):
        tags = get_trending_tags()
        print(f"[{self.name}] scouting tags: {[t['name'] for t in tags]}")
