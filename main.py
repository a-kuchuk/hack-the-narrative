import threading
from bots.article.article_bot import ArticleBot
from bots.reply.reply_bot import ReplyBot
from bots.influencer.influencer_bot import InfluencerBot
from bots.amplifier.amplifier_bot import AmplifierBot
from bots.political.political_bot import PoliticalBot
from bots.npc.npc_bot import NPCBot

def start_bot(bot_class, *args, **kwargs):
    """Start a bot in its own thread."""
    bot = bot_class(*args, **kwargs)
    t = threading.Thread(target=bot.run, daemon=True)
    t.start()
    return t

if __name__ == "__main__":
    bots = [
        start_bot(ArticleBot, "ArticleBot", check_interval=60),
        start_bot(ReplyBot, "ReplyBot", interval=300),
        start_bot(InfluencerBot, "InfluencerBot", interval=3600),
        start_bot(AmplifierBot, "AmplifierBot", interval=300),
        start_bot(PoliticalBot, "PoliticalBot"),
    ]

    print("All bots are running. Press Ctrl+C to exit.")
    
    try:
        while True:
            # Keep main thread alive
            pass
    except KeyboardInterrupt:
        print("Exiting bots...")
