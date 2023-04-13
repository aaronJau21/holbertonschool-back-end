#!/usr/bin/python3
''' Return information about his/her TODO list progress from an REST API '''
import requests
import sys

# Get the employee ID from the command line arguments
if len(sys.argv) < 2:
    print("Please provide an employee ID as a command line argument")
    sys.exit(1)

employee_id = sys.argv[1]

# Make a request to the API to get the employee's TODO list
response = requests.get(
    f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

# Parse the response JSON to get the necessary information
todos = response.json()

total_tasks = len(todos)
completed_tasks = sum(todo['completed'] for todo in todos)

# Print the employee TODO list progress
print(
    f"Employee {todos[0]['userId']} is done with tasks({completed_tasks}/{total_tasks}):")

# Print the titles of completed tasks
for todo in todos:
    if todo['completed']:
        print(f"\t{todo['title']}")
