#!/usr/bin/python3
""" export data in the json format using T0 """

import json
import requests
import sys

if __name__ == "__main__":

    employee_ID = sys.argv[1]
    file_name = employee_ID + ".json"
    user = requests.get(
                        'https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_ID)
                        ).json()
    todos = requests.get(
                        'https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(employee_ID)
                        ).json()
    task_dict = {}
    task_list = []

    for task in todos:
        dict = {"task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")}
        task_list.append(dict)
    task_dict[employee_ID] = task_list

    with open(file_name, 'w') as f:
        json.dump(task_dict, f)
