import requests,json
import pickle 

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

users = json.loads(response.text)

with open('users.pkl','wb') as fpWriter: # wb - write in binary
    pickle.dump(users,fpWriter)
    print('Done pickling')

try:
    with open('users.pkl','rb') as fpreader:
        data = pickle.load(fpreader)
        print("From Pickle", data)
except pickle.UnpicklingError as ex:
    print(ex)