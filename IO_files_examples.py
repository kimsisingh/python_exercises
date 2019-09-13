#Input/Output Files in Python
# When you read a file, you have to close it as well
# Open a file
myfile = open('myfile.txt')
# Read the contents of a file in one huge string
contents = myfile.read()
print(f"Contents of file {contents}")
myfile.seek(0) # to move the cursor back to the starting position
contents_again = myfile.read()
print(f"Contents of file again : \n{contents_again}") # \nPrint in a new line
contents_again1 = myfile.read()
print(f"Contents of file again and there's nothing : \n{contents_again1}")
myfile.seek(0) # to move the cursor back to the starting position
contents_again2 = myfile.read()
print(f"Contents of file again after seek(0): \n{contents_again2}")
myfile.seek(0)
# Error below as this file does not exist
#myfile = open('whoops_wrong.txt')
#Use readlines() method to get the lines in one single list
# with separate object/element to be used for indexing
content_readlines = myfile.readlines()
print(f"Contents of file using readlines method: \n{content_readlines}")
#close the file when done working with it
myfile.close()
#open a file from different location
different_loc_file = open('/Users/kimsi/Documents/Kim_python/myfile_jupiter.txt')
read_diff_loc_file = different_loc_file.readlines()
print(f"Contents of a different located file using readlines method: \n{read_diff_loc_file}")
# To avoid using close method everytime for files, use special with statement
# Notice the identation, No longer worry about closing the file
with open('myfile.txt') as my_new_file:
	contents_with = my_new_file.read()
	print(f"Contents of my NEW file using WITH Statement: \n{contents_with}")
# use with with differently_located_file, no worry about closing the file
with open('/Users/kimsi/Documents/Kim_python/myfile_jupiter.txt') as NEW_Loc_File:
	contents_LOC_with = NEW_Loc_File.read()
	print(f"Contents of my NEW LOCATION file using WITH Statement: \n{contents_LOC_with}")
#Permissions in Files (Read/Write/Append)
# Use open method's mode as read-only default
with open('myfile.txt', mode = 'r') as my_file_mode:
	contents = my_file_mode.read()
	print(f"Contents of my file using MODE READ option: \n{contents}")
# Use open method's mode as write-only, and see error as below
#with open('myfile.txt', mode = 'w') as my_file_mode:
	#contents = my_file_mode.read()
	#print(f"Contents of my file using MODE option: \n{contents}")

# a is appending to the files
with open('myfile.txt', mode = 'a') as f:
	f.write('\nSIX ON SIXTH') # cannot store the result from write in a variable
     # The below will error out as the mode is not readable
	#print(f"Contents of my file using MODE APPEND option: \n{f.read()}")

# Read the file after appending
with open('myfile.txt', mode = 'r') as my_file_mode:
	contents_after_append = my_file_mode.read()
	print(f"Contents of my file using MODE READ after appending: \n{contents_after_append}")
# w overwrites the existing files or creates a new one
with open('huhulahhd.txt', mode = 'w') as f:
	f.write("I created gibberish file. Haha!")

# read the file after writing
with open('huhulahhd.txt', mode = 'r') as my_file_mode:
	contents_after_write = my_file_mode.read()
	print(f"Contents of my file using MODE READ after WRITING: \n{contents_after_write}")




