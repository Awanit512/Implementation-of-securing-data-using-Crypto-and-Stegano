
import sys
class Preprocessing:


	# 
	#Convert 128 bits of data that is 128 bit binary string into 32 bits 
	#This function return tuple of 4 binary string of 32 bits each
	def Convert128_to_32bits(self,temp):
		E_I = []
		temp_str=""
		benches = [32,64,96,128]
		for i in range(129) :

			if i in benches:
				E_I.append(temp_str)
				temp_str=""
				if i==128:
					break


			if i in range(0,31):
				temp_str +=temp[i]

			elif i in range(32,63):
				temp_str+=temp[i]

			elif i in range(64,95):
				temp_str+=temp[i]

			else:
				temp_str+=temp[i]

		
		return (E_I[0],E_I[1],E_I[2],E_I[3])





	#This method is to ensure that our binary string length remain as multiple of 128
	def padding_of_text(self,binary_string) :
		length = len(binary_string)
		remainder_length_padding = length%128  #len(binary_string) = Q*128+r
		remainder  = remainder_length_padding
		padd=""
		for i in range(128-remainder):
			padd+="0"

		return (binary_string+padd)










	#this is to extract actual either plain txt ka binary string or cypher txt ka binary string by seeing 
	#first 25 bit of it whihc is appended 
	def extract_real_binary_string(self,appended_string):
		string_length = appended_string[:25]
		length = self.bin_2_dec(string_length)
		actual_string = appended_string[25:25+length]
		return actual_string






	#Before padding we have to prepend length of this binary string which will be later use for decoding this binary string
	#Note this length will be of 25 bit in length so at input of decryption first 25 bit will tell what is the value of length of
	#binary string to be considered for decoding binary string into plain txt. 
	def prepend_length_of_binary_string(self,binary_string):
		length=len(binary_string)
		binary_value_of_length = bin(length).replace("0b","")
		length_of_bin_value = len(binary_value_of_length)
		if length_of_bin_value<=25:
			to_padd = 25-length_of_bin_value
			padd = ""
			for i in range(to_padd):
				padd+="0"
			return padd+binary_value_of_length+binary_string
		else:
			sys.exit()





	#Convert Binary to decimal
	def bin_2_dec(self,binary_val):
		return int(str(binary_val),2)




	#Convert decimal value to binary
	def dec_2_bin(self,decimal_val):
		return bin(decimal_val).replace("0b","")



		


	#
	#This method is take XOR of two binary string each of 32 bits  ## protected member function
	def xor_32bits(self,temp1 ,temp2):
		temp=""
		for i in range(len(temp1)):
			if temp1[i]==temp2[i]:
				temp+="0"
			else :
				temp+="1"

		return temp




	#
	#This method is do circular shift clockwise   
	def clockwise_CircularShift(self,temp,k):
		l =len(temp)
		left=(temp[:l-k])[-1::-1]
		right=(temp[l-k:])[-1::-1]
		temp=left+right
		temp = temp[-1::-1]
		return temp
		








	
	#This method is do circular shift Anti-clockwise   
	def anti_clockwise_CircularShift(self,temp,k):
		l =len(temp)
		left=temp[k-1::-1]
		right=temp[-1:k-1:-1]
		temp=left+right
		temp = temp[-1::-1]
		return temp






	# THis is the best methood for converting /encoding plain ascii text into binary string and decoding it back


	#Encryption of plain text into Binary Text

	#Think to whether to keep this as static or protected member or public 
	#@staticmethod   for making satic method remember to remove self argumnet in function definition else throws error
	def string_2_binary(self,message):
		
		## older code
		# #length = len(text)
		# #text = str(length)+"*"+text


		# byte_array = text.encode()

		# binary_int = int.from_bytes(byte_array, "big")

		# #print("Binary String : ",binary_int )

		# binary_string = bin(binary_int)

		# #print(f"Binary String --> {binary_string}")

		# modified_binary_string = binary_string[2:]

		# #print(f"Binary String Modified --> {modified_binary_string}")
		# #print(f"Lenth of Binary_string : {len(binary_string)}")
		# #print(f"Lenth of Modified Binary_string : {len(modified_binary_string)}")
		# # for i,d in enumerate(list(s.strip())):
		# #   print(i,d)

		# return modified_binary_string





		# # Newer code.
		if type(message) == str:
			return ''.join([ format(ord(i), "08b") for i in message ])
		elif type(message) == bytes or type(message) == np.ndarray:
			return [ format(i, "08b") for i in message ]
		elif type(message) == int or type(message) == np.uint8:
			return format(message, "08b")
		else:
			raise TypeError("Input type not supported")










	#Decryption of binary strinf intu plain text

	#Think to whether to keep this as static or protected member or public 
	#@staticmethod   for making satic method remember to remove self argumnet in function definition else throws error
	def binary_2_string(self,binary_data):


		# Older code..
		# binary_int = int(binary_string, 2)

		# byte_number = (binary_int.bit_length()+7)//8


		# binary_array = binary_int.to_bytes(byte_number, "big")

		# ascii_text = binary_array.decode()
		# # start=-1
		# # for index,letter in enumerate(list(ascii_text.strip())) :
		# # 	if letter=="*" :
		# # 		return ascii_text[index+1:index+1+length] 
		# # 	else:
		# # 		length=10*length+(int(letter))
		# #return "None-->512:: Opps seems something is Wrong or Data loss occured"
		# return ascii_text








		decoded_data = ""
		all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
		for byte in all_bytes:
			decoded_data += chr(int(byte, 2))
			if decoded_data[-5:] == "#####":
				break
		#print(decoded_data)
		return decoded_data[:-5]















