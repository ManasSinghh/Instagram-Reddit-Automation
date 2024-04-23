import requests

from os import getenv
from lib.redis import does_exist, add_key
import praw


def get_random_post():
    """
    Function to get a random post from Reddit
    Returns:
    - Title of the post
    - URL of the post
    """
    subreddit = getenv("SUBREDDIT")
    reddit = praw.Reddit(
    client_id=getenv("REDDIT_CLIENT_ID"),
    client_secret=getenv("REDDIT_CLIENT_SECRET"),
    user_agent="Insta Reddit Automator by Yashraj Narke",
)   
    for summary in reddit.subreddit(subreddit).hot(limit=50):

        # We'll loop through all the posts and we check for the following
        # 1. If the post is a video, we skip it
        # 2. If the post is a NSFW post, we skip it
        # 3. If the post is a spoiler post, we skip it
        # 4. If the post ID exists in Redis, we skip it
        # 5. If the post doesnt have a image, we skip it

        # If no valid post is found, we raise an exception
        # If sentry is enabled, this will be sent to sentry

        if summary.is_video or summary.over_18 or summary.spoiler:
            continue

        if does_exist(summary.id):
            continue
        try:

            if not summary.url.endswith((".jpg", ".png", ".jpeg")):
                continue
        except:
            print("** Failed to get image URL for post**" + summary.id)

        add_key(summary.id)
        return (summary.title, summary.url)

    raise Exception("No valid post found")
