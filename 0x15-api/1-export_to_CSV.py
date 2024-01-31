#!/usr/bin/python3
""" Python script to export data in CSV format """

import csv
import requests
import sys


def convertto_csv(employee_id):
    """
    Exports data in CSV foramt
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
        file_name = f"{employee_id}.csv"
        with open(file_name, 'w', newline='') as csvfile:
            writerObj = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for todo in todos:
                writerObj.writerow([employee_id,
                                    employee_name[0].get("username"),
                                    todo.get("completed"),
                                    todo.get("title")])


if __name__ == "__main__":
    convertto_csv(sys.argv[1])
