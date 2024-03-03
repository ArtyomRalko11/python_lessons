import requests

url = 'http://jsonplaceholder.typicode.com/todos'

response = requests.get(url).json()

completion = {}
completed_count = 0
not_completed_count = 0
for userId in response:

