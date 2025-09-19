from bots.core.api_client import reply_to_post

class ReplyBot:
    def __init__(self, name):
        self.name = name

    def act(self):
        print(f"[{self.name}] would reply to posts here.")
        reply_to_post("dummy_post_id", f"[{self.name}] reply content")
