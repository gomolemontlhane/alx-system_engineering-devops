#!/usr/bin/python3
"""
Script to gather TODO list progress for a given employee ID from a REST API and export to CSV.
"""

import sys
import requests
import csv

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

    # Prepare CSV file name based on employee ID
    csv_filename = '{}.csv'.format(employee_id)

    # Write data to CSV file
    with open(csv_filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            task_completed = task.get('completed')
            task_title = task.get('title')
            csv_writer.writerow([employee_id, employee_name, str(task_completed), task_title])

    print("Data exported to {}".format(csv_filename))
