#!/usr/bin/python3
""" export data in the CSV format using T0
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE" """

import csv
import requests
import sys
from urllib import response

if __name__ == "__main__":

    employee_ID = sys.argv[1]
    response = requests.get(
                        'https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_ID)
                        )
    user = response.json()
    response = requests.get(
                        'https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(employee_ID)
                        )
    todos = response.json()

    with open(f'{employee_ID}.csv', 'w') as f:
        writer = csv.writer(
                            f,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL,
                            lineterminator='\n'
                            )

        for task in todos:
            writer.writerow(
                            [
                             employee_ID,
                             user.get("username"),
                             task.get("completed"),
                             task.get("title")
                             ]
                            )
