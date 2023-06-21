import requests

print(requests.get('http://127.0.0.1:8080/items/0').json())
