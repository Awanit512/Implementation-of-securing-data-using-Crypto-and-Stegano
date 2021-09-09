from Decryption import Decryption
from Encryption import Encryption
from Preprocessing import Preprocessing








def main():
	# For the integration testing I will take plain txt from usr converting into binary string giving it to Encryption block to 
	# encrypt it so that it gives out cypher text. which is tored in image 
	# after extraaction of cypher txt from stegeo img it will be given to the decryption module 
	# Decryptor decrypt it to yield plain txt.

	plain_text = input("Enter a plain text : ")

	#example : This World shall Know Pain

	print(f"Entered plian Txt : {plain_text}")

	preprocessor = Preprocessing()

	#convert to binary
	plain_2_binary_string = preprocessor.string_2_binary(plain_text)

	#append the length in front of 25 bit
	prepended_binary_string = preprocessor.prepend_length_of_binary_string(plain_2_binary_string)

	#padding with zeroes that binary string so that it is a multiple of 128.
	padded_binary_string = preprocessor.padding_of_text(prepended_binary_string)



	#ENCRYPTION
	encryptor = Encryption()	

	print(f"Padded Binary string  pt1_txt --> : {padded_binary_string}")
	print('\n\n')



	cipher_text = ""
	pt1_txt = padded_binary_string


	for i in range(0,len(padded_binary_string),128):
		string_128_bit = padded_binary_string[i:i+128]
		


		#Encryption starts
		EI_S = preprocessor.Convert128_to_32bits(string_128_bit)


		
		keys = "11110111110000001010010111101001101111101000101000000000111111111111000000001111111011011100010101010010101101010101000010111111"
		KEYS = preprocessor.Convert128_to_32bits(keys)
		

		C1 , C2, C3 , C4 =  encryptor.Encrypt(EI_S,KEYS)
		cipher_text += C1 + C2 + C3 + C4 



	print("cipher_text\n",cipher_text)
	print('\n')
	print("pt1_txt\n",pt1_txt)
	print("\n\n")
	ct_text = cipher_text

	#prepended the length of cypher text in front of 25 bit i.e first 25 bit shows length of cypher text 
	prepended_cypher_txt = preprocessor.prepend_length_of_binary_string(cipher_text)

	#padd it now this cypher txt -->prepended_cypher_txt to padded_cypher_txt
	padded_cypher_txt = preprocessor.padding_of_text(prepended_cypher_txt)



	#Now the padded cypher text -->padded_cypher_txt   will go inside the image and image will be called after insertion as 
	#steogo image

	#Now we have to extract LSB of whole image (or it can be modified / optimized further ) 


	cypher_txt_after_extraction = preprocessor.extract_real_binary_string(padded_cypher_txt)




















	#DECRYPTION
	padded_pt_text = ""

	decryptor = Decryption()

	for i in range(0,len(cypher_txt_after_extraction),128):
		cypher_128_bit = cypher_txt_after_extraction[i:i+128]
		#print("###",i , i+128 , string_128_bit)
		#print('\n\n')

		CT_S = preprocessor.Convert128_to_32bits(cypher_128_bit)
		keys = "11110111110000001010010111101001101111101000101000000000111111111111000000001111111011011100010101010010101101010101000010111111"
		KEYS = preprocessor.Convert128_to_32bits(keys)
		#print("\n\nKEYS : ",KEYS)

		#print('\n\n')





		
		E1,E2,E3,E4 =  decryptor.Decrypt(CT_S,KEYS)
		padded_pt_text += E1 + E2 + E3 + E4 



	print("padded_pt_text\n",padded_pt_text)
	print('\n')

	print("Ab bata jara ",end="")
	print(pt1_txt==padded_pt_text)



	#Now extracting actual binary string from padded plain txt
	real_pt_text = preprocessor.extract_real_binary_string(padded_pt_text)

	#Now convert this real plain txt into Ascii text 
	real_plain_text = preprocessor.binary_2_string(real_pt_text)

	print(f"\n\n\n\n\n\n\n\n\n After all the actual text was :--> {real_plain_text}\n\n\n\n\n\n\n\n\n")













def main2():
	p = Preprocessing()
	keys = "11110111110000001010010111101001101111101000101000000000111111111111000000001111111011011100010101010010101101010101000010111111"
	KEYS = p.Convert128_to_32bits(keys)
	#plain_text = "00000001110101111011011011111011110000000111010111101101101111100010111110011101001101110010100001011000100000100111011001001110" 
	plain_text = "00000000000000000000000000000001010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
	print(plain_text)
	EI_S = p.Convert128_to_32bits(plain_text)
	e = Encryption()
	d = Decryption()

	cypher_txt = e.Encrypt(EI_S,KEYS)
	print( "\ncypher_txt ", cypher_txt , "\n\n" )

	e1 ,e2 ,e3 ,e4 = d.Decrypt(cypher_txt , KEYS)
	decrypted_txt = e1+e2+e3+e4
	print("Decrypted Txt : " ,decrypted_txt , "\n\n")
	print(decrypted_txt==plain_text)

	count=0
	for i in range(128):
		if decrypted_txt[i]!=plain_text[i]:
			print(i+1)

			count+=1

	print(count)







# def checking_individual_preprocessor():
# 	print("\n\n\n\n\n\n\n")
# 	pp = Preprocessing()
# 	plain_text = "00000001110101111011011011111011110000000111010111101101101111100010111110011101001101110010100001011000100000100111011001001110"

# 	q1,q2,q3,q4 = pp.Convert128_to_32bits(plain_text)
# 	print("checkig 128 to 32 bit split")
# 	print(q1+q2+q3+q4 == plain_text) 
# 	print("\n\ncheckig anticlock ")
# 	d="1101101100"
# 	print(f"string to reverse {d} into anticlock 2 times : {pp.anti_clockwise_CircularShift(d,2)}")  

# 	print(f"checkig clock  of {d} into clock wise 2 times : {pp.clockwise_CircularShift(d,2)}") 

# 	print("\n\n\nchecking for xor bits")
# 	a="1101100001"
# 	b="1100000111"
# 	print(f"Xor of \n{a}\n{b}\n{pp.xor_32bits(a,b)}")



if __name__ == "__main__" :
	main()
	print("main 1 called")
	# print("Now calling main2")
	# main2()
	# checking_individual_preprocessor()





# 00000000000000000110011111010100011010000110100101110011001000000101011101101111011100100110110001100100001000000111001101101000
# 00000000000000000110011111010100
# 01101000011010010111001100100000
# 01010111011011110111001001101100
# 01100100001000000111001101101000





# cipher_text
#  11111101111100000010100100000110101011110100010101111001101110011000101111100111101101001111100010100100011110101000001111010000


# pt1_txt
#  00000000000000000000011111001000011001010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000



# pt_text
#  00000001110101111011011011111011110000000111010111101101101111100010111110011101001101110010100001011000100000100111011001001110


# False
# awani
