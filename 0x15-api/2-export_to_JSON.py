#!/usr/bin/python3
"""
Script to gather TODO list progress for a given employee ID from a REST API and export to JSON.
"""

import sys
import requests
import json

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

    # Prepare JSON file name based on employee ID
    json_filename = '{}.json'.format(employee_id)

    # Prepare data in JSON format
    json_data = {str(employee_id): []}
    for task in todos_data:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        }
        json_data[str(employee_id)].append(task_dict)

    # Write data to JSON file
    with open(json_filename, mode='w') as jsonfile:
        json.dump(json_data, jsonfile)

    print("Data exported to {}".format(json_filename))
