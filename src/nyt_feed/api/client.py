import os
from pynytimes import NYTAPI

def auth_nyt():
    api_key = os.getenv("NYT_API_KEY")
    nyt = NYTAPI(api_key, parse_dates=True)
    return nyt