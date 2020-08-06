import json

# json_str = '{"name":"tom","age":18}'
# student = json.loads(json_str)
# print(type(student))    # <class 'dict'>
# print(student)  # {'name': 'tom', 'age': 18}

json_str = '[{"name":"tom","age":18,"false":false},{"name":"jerry","age":18}]'
student = json.loads(json_str)
print(type(student))    # <class 'dict'>
print(student)  # [{'name': 'tom', 'age': 18, 'false': False}, {'name': 'jerry', 'age': 18}]




