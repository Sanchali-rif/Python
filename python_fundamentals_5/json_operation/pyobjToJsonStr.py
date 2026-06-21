import json

py_obj={'name': 'Sanchali', 'age': 20, 'is_student': True, 'hobby':None}
json_str=json.dumps(py_obj)
print(json_str)