import argparse
from bots.influencer.influencer_bot import InfluencerBot
from bots.amplifier.amplifier_bot import AmplifierBot
from bots.reply.reply_bot import ReplyBot
from bots.scout.scout_bot import ScoutBot
from bots.political.political_bot import PoliticalBot
from bots.article.article_bot import ArticleBot
from utils.scheduler import run_schedule

def get_bot_instance(role, name):
    bot_mapping = {
        "influencer": InfluencerBot,
        "amplifier": AmplifierBot,
        "reply": ReplyBot,
        "scout": ScoutBot,
        "political": PoliticalBot,
        "article": ArticleBot
    }
    BotClass = bot_mapping.get(role.lower())
    if not BotClass:
        raise ValueError(f"Unknown bot role: {role}")
    return BotClass(name)

def main():
    parser = argparse.ArgumentParser(description="Run a bot on the fake social platform.")
    parser.add_argument("--role", required=True, help="Bot role: influencer, amplifier, reply, scout, npc, political, article")
    parser.add_argument("--name", default="bot1", help="Name of the bot instance")
    parser.add_argument("--posts", type=int, default=1, help="Number of actions to perform")
    args = parser.parse_args()

    bot = get_bot_instance(args.role, args.name)
    run_schedule([bot], posts_per_day=args.posts)

if __name__ == "__main__":
    main()
