# Dictionaries in Python
# are unordered mappings for storing objects. Lists are ordered sequences
# cannot be sorted, or indexed or sliced like Lists
# Key-value pairs where Key is always a string
# Value can be anything : String, int, list, another dictionary etc.
# Use Key-value pair help to grab objects quickly by key name 
# without any hassle to find the index location

my_dict = {'key1' : 'KIMSI', 'key2' : 'SINGH'}
print(f"My Dictionary is : {my_dict}" )
print(f"The Values are : {my_dict['key1']} {my_dict['key2']}" )
grocery_prices = {'apples' : 2.99, 'oranges' : 1.99, 'milk' : 5.80, 'eggs': 4.99}
print(f"The price for 1 pound apple is : {grocery_prices['apples']} and for a dozen eggs is : {grocery_prices['eggs']}" )
mix_data_type_dict = {'k1' : 123, 'k2' : [0,1,2,3], 'k3' : {'k4': 3456}}
#Grab dict from dict, donot nest one dict into another as ['k3'['k4']]; this is wrong. correct below
print(f"Grab the list from dict : {mix_data_type_dict['k2']} and another dict {mix_data_type_dict['k3']['k4']}" )
print(f"Grab the third item from the list from dict : {mix_data_type_dict['k2'][-1]}")
alpha_dict = {'k1' : ['apple', 'boats', 'cucumber', 'drinks']}
print(f"Grab the second alpha item from the list from dict and convert it to upper case: {alpha_dict['k1'][-2].upper()}")
# Add new key-valur pair to the existing dict
alpha_dict['k2'] = "Hello Shopper"
alpha_dict['k3'] = "Collect your receipt"
print(f" Alpha List {alpha_dict}")
print(f" What's new in my alpha list : {alpha_dict['k1']} , {alpha_dict['k2']} , {alpha_dict['k3']}")
#Replace value for a key
alpha_dict['k3'] = " SHOW YOUR ID "
print(f" Replaced 'Collect your receipt' : {alpha_dict['k1']} , {alpha_dict['k2']} , {alpha_dict['k3']}")
# See all keys of the dictionary
print(f" All Keys' : {alpha_dict.keys()}")
# See all Values of the dictionary
print(f" All Values' : {alpha_dict.values()}")
# See Actual pairings key value pair
print(f" All pairings : ' : {alpha_dict.items()}")







