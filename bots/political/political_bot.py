from bots.core.api_client import post_status
from bots.core.ai_client import gen_content

class PoliticalBot:
    """Posts positive campaign messages for your candidate."""
    def __init__(self, name):
        self.name = name

    def act(self):
        system_msg = (
            "You are a political campaign bot. Write respectful, positive messages "
            "highlighting your candidate's vision and policies."
        )
        prompt = "Write a short, positive campaign post for Victor Hawthorne."
        content = gen_content(prompt, system_msg)
        post_status(content)
        print(f"[PoliticalBot] Posted: {content}")
