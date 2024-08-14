#!/usr/bin/python3

""" A function that queries the reddit API and prints the title of the first
hot ports listed for a subreddit """

import requests


def top_ten(subreddit):
    """Function printing titles of 10 hot ports
    Args:
        subreddit: Contains the hot ports being listed """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'FirstRedditApp/1.0 (francisgwaihiga@gmail.com)'}
    queries = {'limit': 10}

    try:
        response = requests.get(
            url=url, headers=headers, params=queries, allow_redirects=False)
        if response.status_code != 200:
            print(None)
        else:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
    except requests.RequestException:
        print(None)
