#!/usr/bin/python3
""" queries the Reddit API """
import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit"""

    response = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                            .format(subreddit),
                            headers = {'User-agent': 'Holberton'},
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")

    for hot_post in response.json()['data']['children']:
        print(hot_post['data']['title'])
