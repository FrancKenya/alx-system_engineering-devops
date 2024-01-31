#!/usr/bin/python3
"""
Python script fetches and exports TODO list for all employees in JSON format.
"""

import json
import requests


def export_all_json():
    """
    Fetches and exports TODO list in json format
    Args:
        employee_id (int): The employees id
    Return:
        None
    """
    url = f'https://jsonplaceholder.typicode.com/users'
    todorl = f"https://jsonplaceholder.typicode.com/todos"

    response = requests.get(url)
    if response.status_code == 200:
        todo_resp = requests.get(todorl)
        users = response.json()
        todos = todo_resp.json()
        json_data = {}
        for user in users:
            emp_id = user.get("id")
            username = user.get("username")
            user_todos = [
                    {
                        "username": username,
                        "task": todo.get("title"),
                        "completed": todo.get("completed")
                    }
                    for todo in todos
                    if todo.get("userId") == emp_id
                    ]
            json_data[emp_id] = user_todos
        file_name = 'todo_all_employees.json'
        with open(file_name, 'w', newline='') as obj:
            output = json_data
            json.dump(output, obj)


if __name__ == "__main__":
    export_all_json()
