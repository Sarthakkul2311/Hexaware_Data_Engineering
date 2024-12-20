import json
jsonstring = '{ "id": 121, "name": "Sarthak", "course": "Cloud Developer"}'
 
student_data =json.loads(jsonstring)
 
print(student_data) 
print(type(student_data))
print(student_data['name'])
print(student_data['course'])