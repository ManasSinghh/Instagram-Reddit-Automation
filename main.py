# If running locally, it's better to use a .env file to store the environment variables.
from dotenv import load_dotenv
load_dotenv()

# Importing Packages
from custom_logger import get_logger
from lib.misc import camelCaseToNormal, PREFIX, TAGS, downloadImage
from os import getenv
from instagrapi import Client
from lib.reddit import get_random_post

TITLE_PROCESSORS = [camelCaseToNormal]

# Setting up Logging
logger = get_logger(__file__)
logger.info("Insta-Reddit Automator by Yashraj Narke")

# Reading ENV
username = getenv("INSTA_USERNAME")
password = getenv("INSTA_PASSWORD")
subreddit = getenv("SUBREDDIT")


if not username or not password or not subreddit:
    logger.error("Please provide all the required ENV variables")
    raise Exception("Please provide all the required ENV variables")

# Checking if SENTRY_URL exists in ENV
if getenv("SENTRY_URL"):
    logger.info("Sentry is enabled")
    import sentry_sdk

    sentry_sdk.init(
        getenv("SENTRY_URL"),  # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )


logger.info(f"Username: {username}")
logger.info(f"Password: {password[0:3]}{'*' * (len(password) - 3)}")
logger.info(f"Subreddit: {subreddit}")
logger.info(
    "Title Processors: "
    + ", ".join([processor.__name__ for processor in TITLE_PROCESSORS])
)

logger.info("Getting Random Post from Reddit")
post = get_random_post()

logger.info(f"Title: {post[0]}")
logger.info(f"URL: {post[1]}")

logger.info("Processing Title")
for processor in TITLE_PROCESSORS:
    post = (processor(post[0]), post[1])

logger.info(f"Processed Title: {post[0]}")

# Downloading Image
logger.info("Downloading Image")
image_path = downloadImage(post[1])
logger.info(f"Image Downloaded at: {image_path}")

logger.info("Logging to Instagram")
# Logging to Instagram
cl = Client()
cl.login(username, password)
logger.info(f"Successfully Logged in as {cl.account_info().full_name}")

logger.info("Uploading Post to Instagram")
media = cl.photo_upload(image_path, caption=f"{post[0]}\n\n{PREFIX}\n\n{TAGS}")
logger.info(f"Successfully Uploaded Post with Media ID: {media.pk}")
logger.info("Logging Out")
cl.logout()
