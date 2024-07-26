import json

from httpx import Client

api_url = 'https://jsonplaceholder.typicode.com/posts'

with Client() as client:
    response = client.get(api_url)

if response.status_code == 200:
    with open('response_data.json', mode='w') as f:
        json.dump(obj=response.json(), fp=f)
