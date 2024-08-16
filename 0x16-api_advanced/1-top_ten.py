#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'custom user agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    for post in posts[:10]:
        print(post.get('data', {}).get('title', ''))
