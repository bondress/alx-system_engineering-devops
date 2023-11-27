#!/usr/bin/python3
"""REST API for TODO list of given employee"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        userId = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[userId] = []
        for task in tasks:
            dictionary[userId].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
