#!/usr/bin/python3
"""Write a function that queries the Reddit API (/rltoken/b-4nD6hwEeNYTwYl5yWNwA) and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Fetches the top 10 posts from a given subreddit
    and prints the titles.

    Args:
        subreddit (str): The name of the subreddit.
    """
    base_url = ('https://www.reddit.com/r/{}/hot.json'
                .format(subreddit))
    params = {'limit': 10}
    headers = {'User-Agent': 'RedditAPIBot/0.1'}

    response = requests.get(base_url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
   
