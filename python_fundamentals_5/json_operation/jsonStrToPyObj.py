import json

json_str='{"name": "Sanchali","age": 20,"is_student": true}'
print(type(json_str))
python_object=json.loads(json_str) #covert json string into python object which is dicstionary
print(type(python_object),python_object)