import json


import json

with open('data.json') as f:
  data = json.load(f)
  data = data['song']

print(len(data))