import requests,json

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

users = json.loads(response.text)
# print(users)

#Memory level serialization
data = json.dumps(users, indent=2)
# print(data)

#file level
with open('users.json','w') as writer:
    json.dump(data,writer)
    print("JSON serialization done")

#deserialization
with open('users.json','r') as reader:
    data2 = json.load(reader)
    print(data2)