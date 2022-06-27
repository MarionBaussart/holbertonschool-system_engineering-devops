#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ function that returns the number of subscribers
    (not active users, total subscribers) for a given subreddit"""

    response = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit),
                            headers = {'User-agent': 'Holberton'},
                            allow_redirects=False)

    if response.status_code == 404:
        return 0
    return response.json()['data']['subscribers']
