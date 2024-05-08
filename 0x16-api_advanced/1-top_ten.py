#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for post in children[:10]:
            print(post['data']['title'])
    else:
        print(None)

# For testing this function from command line
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

