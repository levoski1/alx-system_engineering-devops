#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Fetches the hot posts from a given subreddit recursively

    Args:
        subreddit (str): The name of the subreddit
        hot_list (list): The list of hot posts
        after (str): The after parameter for the next page

    Returns:
        list: The list of hot posts
    """
    base_url = ('https://www.reddit.com/r/{}/hot/.json?&after={}'
                .format(subreddit, after))

    headers = {'User-Agent': 'RedditAPIBot/0.1'}

    response = requests.get(base_url, headers=headers, allow_redirects=False)

    try:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        next_after = data['data']['after']

        if next_after is not None:
            return recurse(subreddit, hot_list, after=next_after)
        else:
            return hot_list

    except Exception as e:
        return None
