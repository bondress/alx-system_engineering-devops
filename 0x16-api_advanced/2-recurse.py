#!/usr/bin/python3
"""
This module users Reddit's API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """This function returns the top ten post
    titles recursively"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    path = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    prms = {'after': after}
    results = requests.get(path, params=prms, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        titles = results.json().get("data").get("children")
        for title_ in titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
