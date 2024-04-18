import logging
import sys
import os


def get_logger(name : str = "unknown.py"):
    name = os.path.basename(name)
    root = logging.getLogger(name)
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)
    return root