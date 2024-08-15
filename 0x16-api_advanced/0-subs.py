#!/usr/bin/python3

""" A function that  queries the reddit api and returns the number of
subscribers for a given subreddit """

import requests


def number_of_subscribers(subreddit):
    """
    Function querying the reddit API
    Args:
        subreddit - The target query with the number of subscriber to be
        returned
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'FirstRedditApp/1.0 (francisgwaihiga@gmail.com)'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    else:
        data = response.json()
        return data['data']['subscribers']
