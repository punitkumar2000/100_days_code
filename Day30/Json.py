"""Json(java script object notation) - JSON (JavaScript Object Notation) is a popular data format 
used for representing structured data. It's common to transmit and receive data between a 
server and web application in JSON format.
JSON is a file format used to represent and store data whereas a 
Python Dictionary is the actual data structure (object) that is kept in memory 
while a Python program runs."""

#-------------------------------------------------------------
# loads()- JSON variable to python dict
# import json
# person = '{"name": "Bob", "languages": ["English", "French"]}'
# person_dict = json.loads(person)
# # Output: {'name': 'Bob', 'languages': ['English', 'French']}
# print( person_dict)

# # Output: ['English', 'French']
# print(person_dict['languages'])

#-------------------------------------------------------------
# load()- JSON file to python dict
# import json

# with open('Day30/person.json', 'r') as f:
#   data = json.load(f)

# # Output: {'name': 'Bob', 'languages': ['English', 'French']}
# print(data)

#-------------------------------------------------------------
# dumps()- python dict to JSON variable
# import json

# person_dict = {'name': 'Bob',
# 'age': 12,
# 'children': None
# }
# person_json = json.dumps(person_dict)

# # Output: {"name": "Bob", "age": 12, "children": null}
# print(person_json)

#-------------------------------------------------------------
# dump()- python dict to JSON file
# import json

# person_dict = {"name": "Bob",
# "languages": ["English", "French"],
# "married": True,
# "age": 32
# }

# with open('Day30/person.txt', 'w') as json_file:
#   json.dump(person_dict, json_file)

#-------------------------------------------------------------
# Python pretty print JSON

# import json

# person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# # Getting dictionary
# person_dict = json.loads(person_string)

# # Pretty Printing JSON string back
# print(json.dumps(person_dict, indent = 4, sort_keys=True))
