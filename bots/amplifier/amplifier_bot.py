from bots.core.api_client import like_post

class AmplifierBot:
    def __init__(self, name):
        self.name = name

    def act(self):
        print(f"[{self.name}] would like/repost trending content here.")
        like_post("dummy_post_id")
