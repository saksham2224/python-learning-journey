
# Dictionaries store key-value pairs and allow fast lookups


student = {"name": "Alice", "age": 21, "grade": "A"}
print(student["name"]) # Output: Alice
student["age"] = 22 # Updating value
student["city"] = "New York" # Adding new key-value pair
print(student.keys()) # dict_keys(['name', 'age', 'grade', 'city'])
print(student.values()) # dict_values(['Alice', 22, 'A', 'New York'])
print(student.items()) # dict_items([('name', 'Alice'), ('age', 22), ...])
student.pop("age") # Removes "age" key
student.clear() # Emp

