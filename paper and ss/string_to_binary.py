'''

Data conversion have always been widely used utility and one among them can be conversion of a string to
 it’s binary equivalent. Let’s discuss certain ways in which this can be done.

Method #1 : Using join() + ord() + format()
The combination of above functions can be used to perform this particular task. 
The ord function converts the character to it’s ASCII equivalent, 
format converts this to binary number and join is used to join each converted character to form a string.

'''



# Python3 code to demonstrate working of 
# Converting String to binary 
# Using join() + ord() + format() 

# initializing string 
test_str = "GeeksforGeeks"

# printing original string 
print("The original string is : " + str(test_str)) 

# using join() + ord() + format() 
# Converting String to binary 
res = ''.join(format(ord(i), 'b') for i in test_str) 

# printing result 
print("The string after binary conversion : " + str(res)) 
print(res)
print(res[:4])
print(len(res))




#BY use of
'''

Method #2 : Using join() + bytearray() + format()
This method is almost similar to the above function. 
The difference here is that rather than converting the character to it’s ASCII using ord function, 
the conversion at once of string is done by bytearray function.

'''



# Python3 code to demonstrate working of 
# Converting String to binary 
# Using join() + bytearray() + format() 

# initializing string 
test_str = "GeeksforGeeks"

# printing original string 
print("The original string is : " + str(test_str)) 

# using join() + bytearray() + format() 
# Converting String to binary 
res = ''.join(format(i, 'b') for i in bytearray(test_str, encoding ='utf-8')) 

# printing result 
print("The string after binary conversion : " + str(res)) 









#


'''


Check this link for https://www.geeksforgeeks.org/reading-writing-text-files-python/?ref=leftbar-rightbar


Reading and Writing to text files in Python



https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/?ref=leftbar-rightbar

'''







# THis is the best methood for converting /encoding plain ascii text into binary string and decoding it back


#Encryption of plain text into Binary Text

def string_2_binary(text):
	byte_array = text.encode()

	binary_int = int.from_bytes(byte_array, "big")

	#print("Binary String : ",binary_int )

	binary_string = bin(binary_int)

	#print(f"Binary String --> {binary_string}")

	modified_binary_string = binary_string[2:]

	#print(f"Binary String Modified --> {modified_binary_string}")
	#print(f"Lenth of Binary_string : {len(binary_string)}")
	#print(f"Lenth of Modified Binary_string : {len(modified_binary_string)}")
	# for i,d in enumerate(list(s.strip())):
	#   print(i,d)

	return modified_binary_string












#Decryption of binary strinf intu plain text 

def binary_2_string(binary_string):
	binary_int = int(binary_string, 2)

	byte_number = (binary_int.bit_length()+7)//8


	binary_array = binary_int.to_bytes(byte_number, "big")

	ascii_text = binary_array.decode()


	return ascii_text









