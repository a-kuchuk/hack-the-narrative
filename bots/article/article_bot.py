from bots.core.api_client import reply_to_post, get_trending_tags

class ArticleBot:
    """Bot that comments on articles or news posts (stub only)."""
    def __init__(self, name):
        self.name = name

    def act(self):
        tags = get_trending_tags()
        tag = tags[0]["name"] if tags else "Kingston"
        content = f"[{self.name}] interesting take on latest news! #{tag}"
        print(f"[ArticleBot] Would comment: {content}")
        reply_to_post("dummy_article_id", content)
