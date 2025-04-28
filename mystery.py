# import pandas as pd
# df= pd.read_csv('data.csv')
# print(df)

# Dictionaries
student={}
# For List=[], for dictionaries={}
# name,age, gender
student={"name":"Rashi","age":22,"gender":"Female","qualified":True}

# accessing values-u have to give key
student["name"]='Baibhav'
student["age"]=23
student["gender"]='male'
print(student["name"])

# Loop through the disctionaries
for value in student.values():
    print(value)
for k,v in student.items():
    print(k,v)
if 'name' in student:
    print("found key")
#  Merge Dictionaries
employee={'nick name':'Rashi','birth age':22,'biological gender':'Female', 'selected':True}
student.update(employee)
merged = student | employee
print(student)
# create dict from 2 list
keys = ["name", "age", "city"]
values = ["Bob", 30, "Chicago"]
person = dict(zip(keys, values))
print(person)
# Get all # import pandas as pd
# df= pd.read_csv('data.csv')
# print(df)

# Dictionaries
student = {
    "name": "Rashi",
    "age": 22,
    "gender": "Female",
    "qualified": True
}

# accessing values-u have to give key
student["name"] = 'Baibhav'
student["age"] = 23
student["gender"] = 'male'
print(student["name"])

# Loop through the dictionaries
for key, value in student.items():
    print(f"{key}: {value}")

if "name" in student:
    print("Found key")

# Merge Dictionaries
employee = {
    "nick name": "Rashi",
    "birth age": 22,
    "biological gender": "Female",
    "selected": True
}
student.update(employee)
merged = {**student, **employee}
print(student)

# create dict from 2 list
keys = ["name", "age", "city"]
values = ["Bob", 30, "Chicago"]
person = dict(zip(keys, values))
print(person)

# Get all 
print(student.items())
print(student.keys())
print(student.values())
