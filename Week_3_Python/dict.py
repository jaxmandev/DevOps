### Dictionaries
# Mutable, add, remove, pop, alter
# Only one unique key allowed
# Syntax: {key: value}

# Create example dictionary
some_dict = {"key": "value", "name": "hubert", "foo": "bar"}

# Accessing a key / value
some_dict["key"]  # => value
some_dict.get("key")  # => value

# Accessing only the keys
some_dict.keys()

# Accessing only the values
some_dict.values()

# Accessing all the pairs as tuples
some_dict.items()

# Changing a value
some_dict["name"] = "Dev"

# Add new key to dictionary
some_dict["gender"] = "male"

# Removes the specified key
# Returns the value when assigned to a variable
some_dict.pop("key")
del some_dict["name"]

# Clear all key-value pairs
some_dict.clear()

## TASK ##
example_dict = {
    "key": "value",
    "name": "james",
    "lessons": 4,
    "lesson_names": ["operators", "data types", "variables"],
}

# Accessing a list within a dictionary
example_dict["lesson_names"][1]  # => data types


## TASK 2 ##
user_details = {
    "first_name": "Hubert",
    "last_name": "Dev",
    "dob": "01/01/2001",
    "address": "100 Some Road",
    "course": "DevOps",
    "grades": ["A", "A", "B"],
    "hobbies": ["skating", "gaming", "coding"],
}

# Adding an item to "hobbies" list
user_details["hobbies"].append("sleeping")

# Removing an item from "hobbies" list
user_details["hobbies"].remove("gaming")

print(user_details["hobbies"])
