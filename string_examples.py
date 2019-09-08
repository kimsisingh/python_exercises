print('hello world')
print(2+2) #Addition
print('2' + '3') #String Concatenation
print(7/4) # Division
print(7%4) # Remainder to check if even or odd
print(2 ** 3) # 2 to the power of 3
print(2 + 10 * 10 + 3 ) # basic order of operations
print((2 + 10) * (10 + 3)) # the way you want
my_dogs = 2
my_dogs = ["Sammy", "Frankie"] # totally OK as Dynamic Typing in Python
#No Restrictions on data type . In other languages, there is static typing
# Pros of Dynamic : Saves time, makes code readbale
# Cons : may result in bugs due to the unexpected data type.

my_str_kim = "Hello, My name is Kimsi Singh"
print("lalalalalalal")
print(my_str_kim)
my_num=5
print ("Original my_num is")
print (my_num) #Assign names and variables
my_num = 15
print ("my_num now is " )
print( my_num)
my_num = (my_num + my_num)
print("my_num + my_num now is " )
print(my_num) 
my_num = "Well, My_num, now is a String!"
print("Whats my_num now? " + my_num)
print("Indexing Trial, letter at index zero " + my_num[0])
print("Indexing : Fetch the letter S at index 23 : " + my_num[23])
print("Reverse Indexing : Fetching letter S again at index -7 : " + my_num[-7])
print("String slicing by grabbing the string from My_num till the end: " + my_num[6:])
print("String slicing by grabbing the string from beginning till well: " + my_num[:4])
print("Step or jump by 2: " + my_num[:: 2])
print ("Reverse the entire string " +my_num[::-1])
# Strings in Python are immutable; does not support Item assignment
name = "Sam"
#Change Sam to Pam; cannot do name[0] = 'P' as strings are immuable in Python
print("what's my name here: " + name)
last_letters = name[1:]
new_name = "P" + last_letters
print("Whats's my new name: " + new_name)
print("Upper case of my string : " + my_str_kim.upper())
print("Lower case of my string : " + my_str_kim.lower())
print("Split on the White space, by default") # cannot print in the same line
# as split function returns data type 'list' and it cannot concatenate with string
print(my_str_kim.split())
#Split on the S, by default
#print("Split my string on letter s : " + my_str_kim.split('i'))
# The above line won't work for the same reason : str not supported with list
print("Split my string on letter i : ")
print (my_str_kim.split('i'))
print("Split my string on letter s : ")
print (my_str_kim.split('s'))

# String interpolation : Inject a variable into a string
my_variable1 = 'Jinnah'
print ('The first PM of Pakistan was ' + my_variable1)
print('Using format method assigning variables, My name is {j} and my age is {a}'.format(j='John',a='75'))
print('Usinf format method indexing by default, Hey! {} {} {} {} {}? '.format("What's", "in", "the", "dinner", "tonight"))
print('Using Indexing we have the first item as {0} and second as {1}'.format('Toilet Paper', 'Plunger'))
#Floating number precision
result = 100/777
age = 30
print ("Float Formating, The result is {r} ".format(r=result)) # Yay! concatenated str + float
print ("Bring precision in result with value which is r colon width for the white space and precision 4 places as in 4f {r:5.4f} ".format(r=result))
#Using fstrings in python 3.6
print (f"Using FStrings , the name is :  {my_str_kim} and integer age in same print stat is : {age}.")
print (f"Using FStrings concatenated str + float in print , the float number result is  : {result}")
print (f"Using FStrings, concat lists returned by split & string in print stat , the name is  : {my_str_kim.split('s')}")
print (f"Using FStrings , the length  of my name is :  {len(my_str_kim)} and type of my name is : {type(my_str_kim)}.")

#COMPLETE STRING EXERCISE







