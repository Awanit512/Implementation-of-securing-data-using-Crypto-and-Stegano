#import all the required libraries
import sys

ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'

if ros_path in sys.path:

    sys.path.remove(ros_path)

import cv2

sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')


import numpy as np
import types


class STEANOGRAPHY:



	def messageToBinary(self,message):
	  if type(message) == str:
	    return ''.join([ format(ord(i), "08b") for i in message ])
	  elif type(message) == bytes or type(message) == np.ndarray:
	    return [ format(i, "08b") for i in message ]
	  elif type(message) == int or type(message) == np.uint8:
	    return format(message, "08b")
	  else:
	    raise TypeError("Input type not supported")








	def bin_2_dec(self,binary_val):
	  return int(str(binary_val),2)




	# Function to hide the secret message into the image
	#give input file name and the cipher txt 
	def hideData(self,image, cypher_text):
	  flag=True

	  # calculate the maximum bytes to encode
	  n_bytes = image.shape[0] * image.shape[1] * 3 // 8
	  print("Maximum bytes to encode:", n_bytes)

	  #Check if the number of bytes to encode is less than the maximum bytes in the image
	  if len(cypher_text) > n_bytes:
	      raise ValueError("Error encountered insufficient bytes, need bigger image or less data !!")
	  
	  #secret_message += "#####" # you can use any string as the delimeter

	  data_index = 0
	  # convert input data to binary format using messageToBinary() fucntion
	  binary_secret_msg = cypher_text

	  data_len = len(binary_secret_msg) #Find the length of data that needs to be hidden
	  for values in image:
	      for pixel in values:
	       


	          # convert RGB values to binary format
	          r, g, b = self.messageToBinary(pixel)
	          # modify the least significant bit only if there is still data to store
	          if data_index < data_len:
	              # hide the data into least significant bit of red pixel
	              pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
	              data_index += 1
	          if data_index < data_len:
	              # hide the data into least significant bit of green pixel
	              pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
	              data_index += 1
	          if data_index < data_len:
	              # hide the data into least significant bit of  blue pixel
	              pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
	              data_index += 1
	          # if data is encoded, just break out of the loop
	          if data_index >= data_len:
	              break

	  return image





	def showData(self,image):

	  binary_data = ""
	  for values in image:
	      for pixel in values:
	          r, g, b = self.messageToBinary(pixel) #convert the red,green and blue values into binary format
	          binary_data += r[-1] #extracting data from the least significant bit of red pixel
	          binary_data += g[-1] #extracting data from the least significant bit of red pixel
	          binary_data += b[-1] #extracting data from the least significant bit of red pixel
	  # # split by 8-bits
	  # all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
	  # # convert from bits to characters
	  # decoded_data = ""
	  # for byte in all_bytes:
	  #     decoded_data += chr(int(byte, 2))
	  #     if decoded_data[-5:] == "#####": #check if we have reached the delimeter which is "#####"
	  #         break
	  # #print(decoded_data)
	  print(binary_data[:25])
	  KK = binary_data[:153]
	  print(KK)
	  
	  lens=""
	  k=25
	  for i in range(k):
	    lens+=binary_data[i]
	  
	  print("lens")
	  print(lens)


	  cipher_txt=''
	  length = self.bin_2_dec(lens)
	  j=len(binary_data)
	  print(f"length : {length}")
	  for i in range(k,k+length):
	    if i<j:
	      cipher_txt += binary_data[i]

	  return lens+cipher_txt #remove the delimeter to show the original hidden message





	# Encode data into image 
	def encode_text(self,directory,filename1,cypher_text): 
	  image_name = directory+filename1 
	  image = cv2.imread(image_name) # Read the input image using OpenCV-Python.
	  #It is a library of Python bindings designed to solve computer vision problems. 
	  
	  #details of the image
	  print("The shape of the image is: ",image.shape) #check the shape of image to calculate the number of bytes in it
	  #print("The original image is as shown below: ")
	  resized_image = cv2.resize(image, (500, 500)) #resize the image as per your requirement
	  #cv2_imshow(resized_image) #display the image
	  
	      
	  #data = input("Enter data to be encoded : ") 
	  #if (len(data) == 0): 
	    #raise ValueError('Data is empty')
	  
	  #filename = input("Enter the name of new encoded image(with extension): ")
	  filename2 = 'stego_'+filename1
	  encoded_image = self.hideData(image, cypher_text) # call the hideData function to hide the secret message into the selected image
	  cv2.imwrite(directory+filename2, encoded_image)




		  # Decode the data in the image 
	def decode_text(self,directory,filename):
	  # read the image that contains the hidden image
	  #image_name = input("Enter the name of the steganographed image that you want to decode (with extension) :") 
	  image_name = directory+filename
	  image = cv2.imread(image_name) #read the image using cv2.imread() 

	  print("The Steganographed image is as shown below: ")
	  resized_image = cv2.resize(image, (500, 500))  #resize the original image as per your requirement
	  #cv2_imshow(resized_image) #display the Steganographed image
	  
	  binary_data = self.showData(image)
	  return  binary_data






	# Image Steganography         
	def Steganography(self,option,filename,c_text,directory): 
	    #a = input("Image Steganography \n 1. Encode the data \n 2. Decode the data \n Your input is: ")
	    userinput = int(option)
	    if (userinput == 1):
	      print("\nEncoding....")
	      #filename = input("Name of image file with .png extension : ")
	      #c_text = input("Enter Cypher text : ")
	      self.encode_text(directory,filename,c_text) 
	          
	    elif (userinput == 2):
	      print("\nDecoding....") 
	      #filename2 = input("Name of stegeo image to decode : ")
	      cypher_txt =self.decode_text(directory,filename)
	      print("Decoded message is " + cypher_txt) 
	      return cypher_txt 
	    else: 
	        raise Exception("Enter correct input") 
	          


if __name__ == "__main__":
	s=STEANOGRAPHY()
	directory=""
	option=input("Image Steganography \n 1. Encode the data \n 2. Decode the data \n Your input is: ")
	if option==1:
		filename = input("Name of image file with .png extension : ")
		c_text = input("Enter Cypher text : ")
		s.Steganography(option,filename,c_text,directory) 
	else:
		filename2 = input("Name of stegeo image to decode : ")
		c_text=""
		cypher_txtx = s.Steganography(option,filename2,c_text,directory)

	s.Steganography() 