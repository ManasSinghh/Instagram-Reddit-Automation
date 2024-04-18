import requests

from os import getenv
from lib.redis import does_exist, add_key

def get_random_post():
    """
    Function to get a random post from Reddit
    Returns:
    - Title of the post
    - URL of the post
    """
    subreddit = getenv("SUBREDDIT")

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    # Error if status code is not 200
    res.raise_for_status()
    data = res.json()

    # Getting all posts
    posts = data["data"]["children"]
    # Removing First Post
    posts = posts[1:]

    # We'll loop through all the posts and we check for the following
    # 1. If the post is a video, we skip it
    # 2. If the post is a NSFW post, we skip it
    # 3. If the post is a spoiler post, we skip it
    # 4. If the post ID exists in Redis, we skip it
    # 5. If the post doesnt have a image, we skip it

    for post in posts:
        post_data = post["data"]
        if (
            post_data["is_video"] # Check if the post is a video
            or post_data["over_18"] # Check if the post is NSFW
            or post_data["spoiler"] # Check if the post is a spoiler
            or post_data["hidden"] # Check if the post is hidden
            or post_data["post_hint"] != "image" # Check if the post is a image
        ):
            continue

        # If the post passes all the checks, we check if the post ID exists in Redis
        # If it exists, we skip it
        if does_exist(post_data["id"]):
            continue
        
        # If the post ID does not exist in Redis, we set the post ID in Redis
        add_key(post_data["id"])
        return post_data["title"], post_data["url"]
    # If no valid post is found, we raise an exception
    # If sentry is enabled, this will be sent to sentry
    raise Exception("No valid post found")
