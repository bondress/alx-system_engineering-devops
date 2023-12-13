#!/usr/bin/python3
"""This module uses the Reddit API"""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """This function counts all words"""

    if after == "":
        count = [0] * len(word_list)

    path = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(path,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for n in range(len(word_list)):
                    if word_list[n].lower() == word.lower():
                        count[n] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for n in range(len(word_list)):
                for o in range(n + 1, len(word_list)):
                    if word_list[n].lower() == word_list[o].lower():
                        save.append(o)
                        count[n] += count[o]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        aux = count[i]
                        count[i] = count[j]
                        count[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux

            for n in range(len(word_list)):
                if (count[n] > 0) and n not in save:
                    print("{}: {}".format(word_list[n].lower(), count[n]))
        else:
            count_words(subreddit, word_list, after, count)
