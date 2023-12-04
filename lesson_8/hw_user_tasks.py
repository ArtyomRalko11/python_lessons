import requests as req



url = 'https://jsonplaceholder.typicode.com/'
todos = req.get(url + 'todos').json()
users = req.get(url + 'users').json()
    
users_list = {}

for user in users:
    users_list[user['id']] = {'name': user['name']}

print(users_list)

quantity = 0
for todo in todos:
    if todo['userId'] == 5:
        quantity += 1
        
user_tasks = {}
for task in todos:
    if task['completed']:
        if task['userId'] not in user_tasks:
            user_tasks[task['userId']] = 1
        else: 
            user_tasks[task['userId']]
        
print(user_tasks)

for user_id in users_list:
    person = users_list[user_id]
    person['completed'] = 0
    person['not_completed'] = 0
    person['psi'] = 0
    for todo in todos:
        if todo['userId'] == user_id:
            if todo['completed']:
                person['completed'] += 1
            else:
                person['not_completed'] += 1
            person['psi'] = person['completed'] / (person['completed'] + person['not_completed'])

                
print(users_list)



