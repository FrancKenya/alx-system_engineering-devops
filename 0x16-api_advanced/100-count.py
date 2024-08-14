#!/usr/bin/python3

"""A function that recursively queries the Reddit API to count keyword
occurrences in hot articles"""

import requests


def count_words(subreddit, word_list=None, after="", dic={}):
    """ Recursively queries the Reddit API to count keyword
    occurrences in hot articles """

    if word_list is None:
        word_list = set([word.lower() for word in word_list])

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after}
    headers = {'User-Agent': 'FirstRedditApp/1.0 (francisgwaihiga@gmail.com)'}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title'].lower().split()
        for word in word_list:
            dic[word] = dic.get(word, 0) + title.count(word)

    after = data['data']['after']
    if after is not None:
        count_words(subreddit, word_list, after, dic)
    else:
        word_list.sort(key=lambda x: dic.get(x), reverse=True)
        for word in word_list:
            if dic.get(word):
                print("{}: {}".format(word, dic.get(word)))
