import json


# ex.1
# JSON string:
jsonData = '''{
    "Name": "Dami Lee",
    "Contact Number": 123456789,
    "Email": "dami@gmail.com",
    "Hobbies":["Reading", "Watching Soccer", "Traveling"]
    }'''
  
# parse x:
res = json.loads(jsonData)
  
# the result is a Python dictionary:
print(res)

'''
{'Contact Number': 123456789, 'Hobbies': ['Reading', 'Watching Soccer', 'Traveling'], 'Name': 'Dami Lee', 'Email': 'dami@gmail.com'}
'''


# ex.2
# JSON string 
player ='{"id":"72", "name": "CYLee", "team":"UHFC"}'
    
# Convert string to Python dict 
player_dict = json.loads(player) 

print(player_dict) 
# {'team': 'UHFC', 'id': '72', 'name': 'CYLee'}
    
print(player_dict['name']) # CYLee
