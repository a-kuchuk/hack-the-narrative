import time
import random

def run_schedule(bots, posts_per_day=1):
    for bot in bots:
        for _ in range(posts_per_day):
            bot.act()
            time.sleep(random.randint(1, 2))
