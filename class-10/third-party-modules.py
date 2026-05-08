
# External Module

# pip install request


import requests
response = requests.get("https://www.example.com")
print(response.status_code)


response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.status_code)
print(response.json())

