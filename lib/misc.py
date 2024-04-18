import re
from os import getenv, path
import requests

def camelCaseToNormal(text):
    """
    Function to convert camelCase to Normal
    Args:
    - text (str): The text to convert
    Returns:
    - str: The converted text
    """
    
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

# Prefix for the caption
PREFIX = f"Follow @{getenv('INSTA_USERNAME')} for more"

# Tags for the caption (Comes at the end)
TAGS = """----------------------------------------
#programmer #programming #coding #developer #elonmusk
#coder #programmingofficial #meme #java #javascript #python
#webdeveloper #php #software #softwaredeveloper
#computerscience #tech #webdesign #gaming
#technology #webdevelopment #engineer #development
#machinelearning #programmers #softwareengineer
#programmingmemes #computerengineering #pythonprogramming
#stackoverflow
----------------------------------------"""

def downloadImage(url):
    """
    Function to download the image
    Args:
    - url (str): The URL of the image
    Returns:
    - str: The path of the downloaded image
    """
    # Checking if ./temp folder exists
    if not path.exists("./temp"):
        # Creating ./temp folder
        path.mkdir("./temp")

    # Getting the image
    image = requests.get(url)

    # Saving the image
    with open("./temp/image.jpg", "wb") as file:
        file.write(image.content)

    return "./temp/image.jpg"
    