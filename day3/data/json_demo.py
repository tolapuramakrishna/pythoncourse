import json

#deserialization
with open('states.json') as f:
    data = json.load(f)

for state in data.get('states'):
    del state['area_codes']

with open('new_states.json','w') as w:
    json.dump(data,w)