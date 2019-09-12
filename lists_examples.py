# Lists in Python
my_list_int = [1,2,3]
my_list_mix = ['KIM', 'ARROGANT', 100, 23.2]
# Lists can have mixed object types
# Lists have ordered sequences
#Print Length of the lists using 2 printing formats
print (f"Using FString, Length of my_list_int is :  {len(my_list_int)} and type: {type(my_list_int)}")
print ("Using dot format, Length of my_list_mix is : {l} and type is : {t}" .format(l=len(my_list_mix), t = type(my_list_mix)))
#indexing and slicing in lists is same as Strings
print(f"Entry at index 1 {my_list_mix[1]}")
#Slicing in Lists
print(f"Grab only the last 3 entries of the list {my_list_mix[1:]}")
# Concatenate Lists with Lists
my_new_list = ['four', 'five']
my_updated_list = my_list_mix + my_new_list
print(f"New Updated List is : {my_updated_list} ")
#The only difference from strings is that lists are mutable
#Meaning, the items/elements can be changed individually in lists
my_updated_list[5] = "NEW ITEM ALL CAPS"
print(f"New Mutated Updated List  is : {my_updated_list} ")
#Append new elements at the back of the list
#append returns nothing, so don't try to store the result in a variable
print ("Type of my_updated_list type is : {t}" .format(t = type(my_updated_list)))
my_updated_list.append("ALL LOWER CASE")
print(f"Appended new item to the list : {my_updated_list} ")
my_updated_list.append("WHAT's up?")
print(f"Appended again new item to the list : {my_updated_list} ")
#Remove the elements from a list; default is the last element from the list
removed_item = my_updated_list.pop()
print(f"Popped item from the the list : {removed_item} ")
print(f"What's remaining in the list : {my_updated_list} ")
#Remove an item from a specific index
removed_item1 = my_updated_list.pop(6)
print(f"Popped item from the the list : {removed_item1} ")
print(f"What's remaining in the list : {my_updated_list} ")
#Sort a list alphabetically
alpha_list = ['a','f', 'c', 'x', 'k', 'i', 'p', 's', 'w']
int_list = [4,7,1,0,8,2,9,5]
alpha_list.sort()
int_list.sort() # This method does not return anything, so don't store this in a variable
print(f"What's my sorted alpha list : {alpha_list} ")
print(f"What's my sorted int list : {int_list} ")
# You can store the result of sort method as below
my_alpha_list = alpha_list
print(f"What's my sorted alpha list stored in a variable: {alpha_list} ")
# Reverse Method for the int list
alpha_list.reverse()
print(f"What's my reversed alpha list : {alpha_list} ")
int_list.reverse()
reversed_int_list = int_list
print(f"What's my reversed int list from a variable: {reversed_int_list} ")





