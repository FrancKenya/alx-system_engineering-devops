#!/usr/bin/python3
""" A python script that exports TO DO data to JSON """

import json
import requests
import sys


def convert_to_json(employee_id):
    """
    Fetches and expoets TO DO list to JSON
    Args:
        employee_id (int): The employees id
    Return:
        None
    """
    url = f'https://jsonplaceholder.typicode.com/users?id={employee_id}'
    todorl = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    response = requests.get(url)
    if response.status_code == 200:
        todo_resp = requests.get(todorl)
        employee_name = response.json()
        todos = todo_resp.json()
        file_name = f"{employee_id}.json"
        json_data = {employee_id: [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee_name[0].get("username")
                }
            for todo in todos
            ]
            }
        with open(file_name, 'w', newline='') as obj:
            output = json_data
            json.dump(output, obj)


if __name__ == "__main__":
    convert_to_json(sys.argv[1])
