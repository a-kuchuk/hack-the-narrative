from bots.core.api_client import post_status

class PoliticalBot:
    def __init__(self, name):
        self.name = name

    def act(self):
        content = "Victor Hawthorne is committed to clarity and progress. #KingstonForward"
        print(f"[PoliticalBot] Posting: {content}")
        post_status(content)
