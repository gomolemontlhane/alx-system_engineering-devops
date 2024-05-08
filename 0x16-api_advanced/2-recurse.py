#!/usr/bin/python3
"""
2-recurse
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for post in children:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None

# For testing this function from command line
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result:
            print(len(result))
        else:
            print("None")

