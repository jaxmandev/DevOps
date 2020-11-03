mix_list=[1,3.14,"raspberry","pi",True,42,False]
print(mix_list)
print(type(mix_list))
print(type(mix_list[0]),type(mix_list[1]),type(mix_list[2]), type(mix_list[3]), type(mix_list[4]), type(mix_list[5]), type(mix_list[6]))

# Add an item
mix_list.append("pie")
print(mix_list)
# Remove an item
mix_list.remove(False)
print(mix_list)
# Replace an item
mix_list[5]=72
print(mix_list)
# Use pop
mix_list.pop()
print(mix_list)

# Print in reverse
print(mix_list[-1], mix_list[-2], mix_list[-3], mix_list[-4], mix_list[-5], mix_list[-6])
