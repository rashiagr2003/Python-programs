# Creating a list
# items=[],items={},items=<>,items=()
items=["speaker", "mobile", "Laptop", "HEADPHONE"]
print(items)
# Negative indexing
print(items[-3])
# Slicing a list
print(items[0:2])
print(items[2:4])
print(items[:2])
# Modifying a List
items[2]="Desktop"
print(items[2])
# Adding element to a list
items.append('charger')
print(items)
# Remove the items del,remove,clear for all items
items.remove('mobile')
del items[-1]
print(items)
items.clear()
# print(items)
items=["speaker", "mobile", "Laptop", "HEADPHONE","charger", "earphone"]
# Checking for the existence
print("earbuds" in items)
# Length of the list
print(len(items))
# List comprehension
# without List comprehension user can convert list element half by for loop
scores=[34,67,45,67,46]
# for i in scores :
#     print(i/2)
# Using List comprehension
print([i/2 for i in scores])
# Combine two list list1+list2, list1.extend(list2)
items.extend(scores)
print(items)