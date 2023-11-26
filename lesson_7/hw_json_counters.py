import requests

url = 'https://jsonplaceholder.typicode.com/todos'
completed_count = 0
not_completed_count = 0
todos_count = 0

response = requests.get(url).json()

for todo in response:
    todos_count += 1
    if todo["completed"]:
        completed_count += 1
    else:
        not_completed_count += 1

percentage = completed_count / not_completed_count * 100



print(f'Total: {todos_count}, Completed: {completed_count}, Not completed: {not_completed_count}, Percentage: {percentage} ')
