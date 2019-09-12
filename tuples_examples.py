#Tuples in Python
#Very similar to lists except that Tuples are immutable
#The element or the value in a tuple cannot be changed or reassigned
#Lists use [] brackets , Tuples use () parenthesis

#Why Tuples and not lists?
#For Data Integrity, where you want to avoid any accidental change of 
#objects/elements in a program, tuple becomes a great solution.


my_tuple = (1,2,3,4,2,5,6,'KIM',7,8,2,2,2,2,9,0, 'KIM')
my_list = [1,2,3,4,5, 0.2, "HELLO"]
print(f"Type of my_tuple : {type(my_tuple)} and length {len(my_tuple)}")
print(f"Type of my_list : {type(my_list)} and length {len(my_list)}")
# Indexing
print(f"Grab element at index 4 of my_tuple {my_tuple[4]}")
print(f"Grab the last element in the tuple {my_tuple[-1]}")

#2 Methods in Tuple
# Index () and Count()
# Index method shows the index location where the elements occurs
# for the first time in the tuple
print(f" Where does 2 occurs for the first time in my_tuple {my_tuple.index(2)}")

# count() method tells how many times an element has been repeated
print(f" How many times 2 occurs in my_tuple {my_tuple.count(2)}")

# CANNOT Reassign the element in tuple as below
#my_tuple[-1] = "KIMSI"



