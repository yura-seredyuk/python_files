import json

file = open('files/data.json', 'r')
# print(file.read())

data = json.loads(file.read())
print(type(data))

for item in data['exchangeRate']:
    print(item)

file.close()