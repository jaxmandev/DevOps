# Python Collections #

### Lists ###
# Mutable, remove, add, change
# Syntax: [var, var2, var3]

# Create an example list
shopping_list = ["apple", "milk", "bread"]

# Indexing list items
shopping_list[0]
shopping_list[1]
shopping_list[2]
shopping_list[-1]
shopping_list[1:3]

# Append adds an item at the end of the list
shopping_list.append("eggs")

# Inserts an item in a specific index
shopping_list.insert(0, "chicken")

# Removes the first occurance of the item in a list
shopping_list.remove("milk")

# Pops a specific index from the list
# Pop stores the poped value in a variable if set
shopping_list.pop(0)

# Replacing an object
shopping_list[1] = "beef"

# Clear the list i.e. remove all items in the list
shopping_list.clear()
