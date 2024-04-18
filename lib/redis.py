from upstash_redis import Redis
redis = Redis.from_env()


def does_exist(key):
    """
    Function to check if a key exists in Redis
    Args:
    - key (str): The key to check
    Returns:
    - bool: True if the key exists, False otherwise
    """
    return redis.exists(key) == 1

def add_key(key):
    """
    Function to add a key in Redis
    Args:
    - key (str): The key to add
    """
    redis.set(key, 1)