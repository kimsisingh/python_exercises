#What are sets?
# They are unordered collection of unique elements, with no repetition
# Use single quotes when adding elements to any data type or in the print
# Use set() method to create an empty set or grab a unique set from lists
# This method does not return any ordered sequence.
my_set = set()
print(f"My set is empty right now : {my_set}")
print(f"Adding element to my set : {my_set.add('SINGH')}")
print(f"My set right now : {my_set}")

print(f"Adding another element to my set : {my_set.add('KIMSI')}")
print(f"My set right now : {my_set}")

print(f"Adding SINGH element again to my set : {my_set.add('SINGH')}")
print(f"My set right now : {my_set}")
print(f"Adding 1 element  to my set : {my_set.add(1)}")
print(f"My set right now : {my_set}")

my_list =[1,2,2,2,2,1,1,1,'KIM', 'SINGH', 34.5, 6.5, 1,3,3,3,3,4,4,45,55,5,8,7,7,7,88,8,88,9,9,9,99,0,00,100] 
# Grab a unique value from this list
print(f"Grab a unique value from this list using sets : {set(my_list)}")






