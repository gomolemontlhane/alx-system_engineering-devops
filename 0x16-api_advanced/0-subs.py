#!/usr/bin/python3
"""
0-subs.py: Gets the number of subscribers for a subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit, or 0 if invalid.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={"User-Agent": "My Reddit API Script"})

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0

if __name__ == "__main__":
    subreddit = input("Enter a subreddit: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"Subscribers: {subscribers}")