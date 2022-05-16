#!/usr/bin/python3
""" export data in the json format for all employees using T0
Format must be: { "USER_ID": [{"task": "TASK_TITLE",
                               "completed": TASK_COMPLETED_STATUS,
                               "username": "USERNAME"},
                         ... ]} """

import json
import requests
import sys

if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get(
                        'https://jsonplaceholder.typicode.com/todos'
                        ).json()
    task_dict = {}

    for usr in user:
        task_list = []
        for task in todos:
            if task.get("userId") == usr.get("id"):
                dict = {"username": usr.get("username"),
                        "task": task.get("title"),
                        "completed": task.get("completed")}
                task_list.append(dict)
        task_dict[usr.get("id")] = task_list

    with open('todo_all_employees.json', 'w') as f:
        json.dump(task_dict, f)
