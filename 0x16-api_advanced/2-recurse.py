#!/usr/bin/python3

""" A recursive function that queries the reddit API
and returns a list containing the titles of all hot articles
for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None, limit=None, count=0):
    """" Recursively queries the reddit API
    Args: subreddit - Contains the hot articles
        hot_list - list to be appended with the hot titles and returned
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after, 'limit': 100}
    headers = {'User-Agent': 'FirstRedditApp/1.0 (francisgwaihiga@gmail.com)'}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        hot_list.append(post['data']['title'])
        count += 1

        if limit and count >= limit:
            return hot_list

    after = data['data']['after']

    if after is not None:
        return recurse(subreddit, hot_list, after, limit, count)
    else:
        return hot_list
