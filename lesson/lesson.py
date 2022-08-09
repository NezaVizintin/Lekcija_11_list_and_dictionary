#-----  LISTS  -----

number_list = [3, 1, 2]
print(number_list)

string_list = ["Harley", "Brincelj", "Legolas"]
print(string_list)

mixed_list = ["Harley", True, 5, 3.14]
print(mixed_list)

# sort items in the list
number_list.sort()

# add items to the end of the list
number_list.append(4)
print(number_list)

# remove items from the list
number_list.pop()
print(number_list)

number_list.pop(0)
print(number_list)

#print items one by one
for item in string_list:
    print(item)

#-----  DICTIONARIES  -----

box = {"height": 20, "width": 45, "length": 30}
print(box["height"])
print(box.get("width"))

# add item (key and value)
box["weight"] = 1
print(box)

# change a value
box["height"] = 40
print(box)

# remove item
box.pop("width")
print(box)

# dictionary can contain a list
pets = {"dogs": "Legolas", "cats": ["Brincelj", "Harley"]}
print(pets)

# a list can contain a dictionary
animals = ["okapi", {"dog": "Legolas"}]
print(animals)