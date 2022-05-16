#!/usr/bin/python3
""" export data in the json format using T0 """
import json
import requests
import sys


if __name__ == "__main__":

    employee_ID = sys.argv[1]
    user = requests.get(
                        'https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_ID)
                        ).json()
    todos = requests.get(
                        'https://jsonplaceholder.typicode.com/todos'
                        ).json()
    task_dict = {}
    task_list = []

    for task in todos:
        if task.get('userId') == int(id):
            dict = {"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.get("username")}
            task_list.append(dict)
    task_dict[employee_ID] = task_list

    with open(f'{employee_ID}.json', 'w') as f:
        json.dump(task_dict, f)
