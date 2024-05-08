#!/usr/bin/python3
"""
A module that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the subscriber count of a given subreddit.
    Returns 0 if the subreddit does not exist.
    """
    api_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyRedditApp/1.0.0'}

    response = requests.get(api_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    return 0
