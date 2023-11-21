import json
import requests as r


url = 'https://jsonplaceholder.typicode.com/todos'
response = r.get(url).json()

for todo in response:
    if not todo["completed"]:
        print(todo)
    
