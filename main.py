import threading
from bots.article.article_bot import ArticleBot, ArticleBotEvil
from bots.reply.reply_bot import ReplyBot, ReplyBotEvil
from bots.influencer.influencer_bot import InfluencerBot
from bots.amplifier.amplifier_bot import AmplifierBot
from bots.political.political_bot import PoliticalBot, PoliticalBotEvil
def print_menu():
    print("\n--- Bot Manual Trigger Menu ---")
    for key, (name, _) in BOTS.items():
        print(f"{key}. Trigger {name}")
    print("0. Exit")

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

    article_evil = ArticleBotEvil("ArticleBot")
    reply_evil = ReplyBotEvil("ReplyBot")
    political_evil = PoliticalBotEvil("PoliticalBot")

    BOTS = {
    "1": ("ArticleEvil", article_evil),
    "2": ("ReplyEvil", reply_evil),
    "3": ("PoliticalEvil", political_evil),
}
    
    try:
        while True:
            print_menu()
            choice = input("Enter choice: ").strip()
            if choice == "0":
                print("Exiting...")
                break
            elif choice in BOTS:
                name, bot = BOTS[choice]
                print(f"Triggering {name}...")
                bot.act()  # Call the single action instead of run loop
            else:
                print("Invalid choice. Try again.")
    except KeyboardInterrupt:
        print("Exiting bots...")
