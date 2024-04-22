import json
import requests

def fetch_all_tasks():
    base_url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(f'{base_url}/users')
    users = response.json()

    tasks_by_user = {}

    for user in users:
        user_id = user['id']
        response = requests.get(f'{base_url}/todos?userId={user_id}')
        tasks = response.json()
        
        tasks_by_user[user_id] = [
            {
                'username': user['username'],
                'task': task['title'],
                'completed': task['completed']
            }
            for task in tasks
        ]
    
    return tasks_by_user

def export_to_json(tasks_by_user):
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(tasks_by_user, json_file, indent=4)

if __name__ == '__main__':
    tasks_by_user = fetch_all_tasks()
    export_to_json(tasks_by_user)
