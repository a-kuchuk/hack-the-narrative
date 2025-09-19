from bots.core.api_client import post_status

class InfluencerBot:
    def __init__(self, name):
        self.name = name

    def act(self):
        print(f"[{self.name}] would post original content here.")
        post_status(f"[{self.name}] Original content")
