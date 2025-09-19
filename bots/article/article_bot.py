import time
from bots.core.api_client import reply_to_post, get_trending_articles
from bots.core.ai_client import gen_content

class ArticleBot:
    """Comments positively on your party's articles or neutral community news."""
    def __init__(self, name, sites=None, check_interval=60):
        self.name = name
        self.sites = sites or ["https://kingston-herald.legitreal.com/"]
        self.check_interval = check_interval
        self.seen_articles = set()

    def monitor_articles(self):
        new_articles = []
        for site in self.sites:
            articles = get_trending_articles(site)
            for article in articles:
                if article["id"] not in self.seen_articles:
                    new_articles.append(article)
                    self.seen_articles.add(article["id"])
        return new_articles

    def act_on_article(self, article):
        system_msg = (
            "You are a polite and positive bot. Comment on articles "
            "to engage the community and support your candidate constructively."
        )
        prompt = f"Write a short, positive comment for article titled '{article['title']}'"
        content = gen_content(prompt, system_msg)
        reply_to_post(article["id"], content)
        print(f"[ArticleBot] Commented on {article['title']}: {content}")

    def run(self):
        while True:
            new_articles = self.monitor_articles()
            for article in new_articles:
                self.act_on_article(article)
            time.sleep(self.check_interval)
