#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODOs list progress """

import requests
import sys
from urllib import response

if __name__ == "__main__":

    employee_ID = sys.argv[1]
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employee_ID))
    user = response.json()
    response = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(employee_ID))
    todos = response.json()

    nb_task_done = 0
    nb_total_task = 0
    task_done = []

    for task in todos:
        nb_total_task += 1
        if task.get("completed") is True:
            nb_task_done += 1
            task_done.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
                                        user.get("name"),
                                        nb_task_done,
                                        nb_total_task))

    for task in task_done:
        print("\t{}".format(task))
