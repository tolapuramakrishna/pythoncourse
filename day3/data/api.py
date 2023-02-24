import requests, json

url = 'http://api.openweathermap.org/data/2.5/weather?q=chennai&units=imperial&appid=ca3f6d6ca3973a518834983d0b318f73'

response = requests.get(url)
# print(response.headers)
report = json.loads(response.text)
# print(type(report)) #clas dict
print(report)
desc = report['weather'][0].get('description')

print(f"In Chennai {desc} now")