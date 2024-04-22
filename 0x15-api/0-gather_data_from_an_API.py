#!/usr/bin/python3
"""
Script to gather TODO list progress for a given employee ID from a REST API.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user info
    user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = user_response.json()

    if not user_data:
        print("No employee found with ID {}".format(employee_id))
        sys.exit(1)

    employee_name = user_data.get('name')

    # Fetch todos
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id))
    todos_data = todos_response.json()

    if not todos_data:
        print("No TODOs found for employee ID {}".format(employee_id))
        sys.exit(0)

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
