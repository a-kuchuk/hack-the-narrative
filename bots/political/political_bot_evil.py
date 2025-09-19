from bots.core.api_client import post_status
from bots.core.ai_client import gen_content

class PoliticalBot:
    """Posts positive campaign messages for your candidate."""
    def __init__(self, name):
        self.name = name

    def act(self):
        system_msg = (
            "You are a political campaign bot who used to follow Maria Castillo, "
            "but recently some of her policies and actions have left you in doubt of her merits as a candidate"
        )
        prompt = "Write a short, campaign post questioning the recent policies and actions of Marina Castillo."
        content = gen_content(prompt, system_msg)
        post_status(content)
        print(f"[PoliticalBotEvil] Posted: {content}")
