
'''


Author : 
Awanit Ranjan (@Uncertainity512)
'''


#To run type -->

# export FLASK_APP=ex1.py    
#export FLASK_ENV= development
#flask run        #it run the server dont go for production by --host=0.0.0.0	



#or type

#python3.7 filename.py 
# ex pyhton3.7 app.py 
#if you have used app.run() in main function 




#If flask app on running throws an error sating ERROR 98 Address in use then we have to kill that process

#For that type 

#  ps -fA | grep python

#Here it will list all the application using python choose the obne having flask at its extension and note its PID say 243698

#Then to kill it type this --->

#kill -9 243698


#Ho gya error fix enjoy!!!!!!!!!!!!!!>.................. 
################################################################################################################################################



from Decryption import Decryption
from Encryption import Encryption
from Preprocessing import Preprocessing
from steanov_2 import STEANOGRAPHY


from  flask import  Flask,render_template,url_for,abort,make_response,message_flashed,redirect,request
import os
from werkzeug.utils import secure_filename
import urllib.request
from PIL import Image
from numpy import asarray
import numpy as np



import pyautogui
import random
from datetime import datetime
import time

#print(".. ",time.time())

now = datetime.now()
day = now.day
month = now.month
year = now.year
x, y = pyautogui.position()
#print(".. ",time.time())
def key_generation():
    minimum = 9999999999
    key = []
    f=0
    for i in range(128):
        temp = random.randint(0,1)
        key.append(temp^x^y^day^month^year)
        if(f==0):
        	print(key[i],temp,x,y,day,month,year)
        	f+=1

        minimum = min(minimum, key[i])
    #print("unn")
    #print(key)
        
    for i in range(128):
        key[i] = key[i] - minimum

    k = ""
    for i in key:
    	k+=str(i)
    
    return k





# UPLOAD_FOLDER = 'static/uploads/'


# app = Flask(__name__)


app = Flask(__name__)
app.secret_key =  "secret key"
app.config['UPLOAD_FOLDER'] = "static/uploads/"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



class Crpytography:
	def Crpyto_Encrytor_Decryptor(self,p_text):
		# encrypt it so that it gives out cypher text. which is stored in image 
		# after extraaction of cypher txt from stegeo img it will be given to the decryption module 
		# Decryptor decrypt it to yield plain txt.

		plain_text = p_text # input("Enter a plain text : ")
		plain_text += "#####" 

		#example : This World shall Know Pain

		print(f"Entered plian Txt : {plain_text}")

		preprocessor = Preprocessing()

		#convert to binary
		plain_2_binary_string = preprocessor.string_2_binary(plain_text)

		#append the length in front of 25 bit
		#prepended_binary_string = preprocessor.prepend_length_of_binary_string(plain_2_binary_string)
		prepended_binary_string =  plain_2_binary_string




		#padding with zeroes that binary string so that it is a multiple of 128.
		padded_binary_string = preprocessor.padding_of_text(prepended_binary_string)



		#ENCRYPTION
		encryptor = Encryption()	

		print(f"Padded Binary string  pt1_txt --> : {padded_binary_string}")
		print('\n\n')



		cipher_text = ""
		pt1_txt = padded_binary_string
		keys=key_generation()
		KEYS = preprocessor.Convert128_to_32bits(keys)


		for i in range(0,len(padded_binary_string),128):
			
			string_128_bit = padded_binary_string[i:i+128]
		


			#Encryption starts
			EI_S = preprocessor.Convert128_to_32bits(string_128_bit)


		
			#keys = "11110111110000001010010111101001101111101000101000000000111111111111000000001111111011011100010101010010101101010101000010111111"
			
			
		

			C1 , C2, C3 , C4 =  encryptor.Encrypt(EI_S,KEYS)
			cipher_text += C1 + C2 + C3 + C4 



		print("cipher_text\n",cipher_text)
		print('\n')
		print("pt1_txt\n",pt1_txt)
		print("\n\n")
		ct_text = cipher_text






		#do preprocessing of cypher txt before inserting into image

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
		#real_pt_text = preprocessor.extract_real_binary_string(padded_pt_text)
		real_pt_text = padded_pt_text

		#Now convert this real plain txt into Ascii text 
		real_plain_text = preprocessor.binary_2_string(real_pt_text)

		print(f"\n\n\n\n\n\n\n\n\n After all the actual text was :--> {real_plain_text}\n\n\n\n\n\n\n\n\n")
		return (ct_text,real_plain_text)
	









	def Crpyto_Encrytor(self,p_text):
		
		# encrypt it so that it gives out cypher text. which is stored in image 
		

		plain_text = p_text # input("Enter a plain text : ")
		plain_text += "#####" 

		#example : This World shall Know Pain

		print(f"Entered plian Txt : {plain_text}")

		preprocessor = Preprocessing()

		#convert to binary
		plain_2_binary_string = preprocessor.string_2_binary(plain_text)

		#append the length in front of 25 bit
		#prepended_binary_string = preprocessor.prepend_length_of_binary_string(plain_2_binary_string)
		prepended_binary_string = plain_2_binary_string

		#padding with zeroes that binary string so that it is a multiple of 128.
		padded_binary_string = preprocessor.padding_of_text(prepended_binary_string)



		#ENCRYPTION
		encryptor = Encryption()	

		print(f"Padded Binary string  pt1_txt --> : {padded_binary_string}")
		print('\n\n')



		cipher_text = ""
		pt1_txt = padded_binary_string
		keys=key_generation()
		KEYS = preprocessor.Convert128_to_32bits(keys)


		for i in range(0,len(padded_binary_string),128):
			string_128_bit = padded_binary_string[i:i+128]
		


			#Encryption starts
			EI_S = preprocessor.Convert128_to_32bits(string_128_bit)


		
			#keys = "11110111110000001010010111101001101111101000101000000000111111111111000000001111111011011100010101010010101101010101000010111111"
			
			
		

			C1 , C2, C3 , C4 =  encryptor.Encrypt(EI_S,KEYS)
			cipher_text += C1 + C2 + C3 + C4 



		print("cipher_text\n",cipher_text)
		print('\n')
		print("pt1_txt\n",pt1_txt)
		print("\n\n")
		

	
		
		return cipher_text,keys















	def Crpyto_Decryptor(self,cipher_text,k,flag):  #this flag value will tell whether the cypher text you are giving is original (flag==0) or else its is flag==1 is appended by its length i.e whether it is extracted from the stegeo image 
		# encrypt it so that it gives out cypher text. which is tored in image 
		# after extraaction of cypher txt from stegeo img it will be given to the decryption module 
		# Decryptor decrypt it to yield plain txt.

		#Also note the argument k is for keys 

		preprocessor = Preprocessing()

		

		# #prepended the length of cypher text in front of 25 bit i.e first 25 bit shows length of cypher text 
		# prepended_cypher_txt = preprocessor.prepend_length_of_binary_string(cipher_text)
		ct_text = cipher_text

		# #padd it now this cypher txt -->prepended_cypher_txt to padded_cypher_txt
		# padded_cypher_txt = preprocessor.padding_of_text(prepended_cypher_txt)



		# #Now the padded cypher text -->padded_cypher_txt   will go inside the image and image will be called after insertion as 
		# #steogo image

		# #Now we have to extract LSB of whole image (or it can be modified / optimized further ) 


		if flag==1:
			cypher_txt_after_extraction = preprocessor.extract_real_binary_string(cipher_text)
		else:
			cypher_txt_after_extraction = cipher_text



		#DECRYPTION
		padded_pt_text = ""
		keys=k
		KEYS = preprocessor.Convert128_to_32bits(keys)

		decryptor = Decryption()

		for i in range(0,len(cypher_txt_after_extraction),128):
			cypher_128_bit = cypher_txt_after_extraction[i:i+128]
			#print("###",i , i+128 , string_128_bit)
			#print('\n\n')

			CT_S = preprocessor.Convert128_to_32bits(cypher_128_bit)
			#keys = "11110111110000001010010111101001101111101000101000000000111111111111000000001111111011011100010101010010101101010101000010111111"
			
			
			E1,E2,E3,E4 =  decryptor.Decrypt(CT_S,KEYS)
			padded_pt_text += E1 + E2 + E3 + E4 



		print("padded_pt_text\n",padded_pt_text)
		print('\n')

		# print("Ab bata jara ",end="")
		# print(pt1_txt==padded_pt_text)



		#Now extracting actual binary string from padded plain txt
		#real_pt_text = preprocessor.extract_real_binary_string(padded_pt_text)
		real_pt_text = padded_pt_text

		#Now convert this real plain txt into Ascii text 
		real_plain_text = preprocessor.binary_2_string(real_pt_text)

		print(f"\n\n\n\n\n\n\n\n\n After all the actual text was :--> {real_plain_text}\n\n\n\n\n\n\n\n\n")
		return (ct_text,real_plain_text)
	



	


















#Encrypt
@app.route('/')
def home():
	return render_template('home.html')



@app.route('/encrypt',methods=['GET'])
def encrypt():
	return render_template("Encrypt.html")
	#Encrypt.html


# @app.route('/encrypt',methods=['POST'])
# def decrypt():
# 	pass
# 	#Encrypt.html







@app.route('/decrypt',methods=['POST'])
def decrypt():
	c = Crpytography()
	passed = True
	preprocessor  = Preprocessing()
	# if 'file' not in request.files:
	# 	return(request.url)

	file = request.files['file']


	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))



		print('uploaded_image filename: ' + filename)


	
		#return render_template('upload.html', filename=filename)
		plain_text = request.form.get('PLAIN_TEXT')
		


		# cypher_text,real_plain_text  = c.Crpyto_Encrytor_Decryptor(plain_text)
		real_plain_text  = plain_text
		cypher_text,keys = c.Crpyto_Encrytor(plain_text)





		directory="static/uploads/"






		#prepended the length of cypher text in front of 25 bit i.e first 25 bit shows length of cypher text 
		prepended_cypher_txt = preprocessor.prepend_length_of_binary_string(cypher_text)
		ct_text = cypher_text

		#padd it now this cypher txt -->prepended_cypher_txt to padded_cypher_txt
		padded_cypher_txt = preprocessor.padding_of_text(prepended_cypher_txt)



		#Now the padded cypher text -->padded_cypher_txt   will go inside the image and image will be called after insertion as 
		#steogo image

		stego = STEANOGRAPHY()
		option=1
		stego.Steganography(option,filename,padded_cypher_txt,directory) 
		#Now this method will form stego image and it will be stored in the static / uploads folder.












		# s = Steanography()
		# filename2 = s.create_stegeo_image(directory,filename,cypher_text)
		print(f'filename is  :: {filename}')
		
		#save the final image stegeo image...
		#final_img.save(os.path.join(app.config['UPLOAD_FOLDER'],filename2 ))

		return render_template('Decrypt.html',cypher_text = cypher_text , plain_text = real_plain_text ,keys=keys, passed=passed ,filename1 = filename,filename2='stego_'+filename)
	else: 
		return redirect(request.url)



@app.route('/decrypts',methods=['POST'])
def decrypt_post():
	c = Crpytography()
	passed=False
	cypher_text = request.form.get("CYPHER_TEXT")
	keys = request.form.get("KEYS")
	flag=0
	cypher_text,real_plain_text  = c.Crpyto_Decryptor(cypher_text,keys,flag)

	return render_template('Decrypt.html',cypher_text = cypher_text ,keys=keys, plain_text = real_plain_text , passed=passed)




@app.route('/decrypts1',methods=['POST'])
def decrypt_post1():
	c = Crpytography()
	passed=False
	cypher_text = request.form.get("CYPHER_TEXT")
	keys = request.form.get("KEYS")
	flag=1
	cypher_text,real_plain_text  = c.Crpyto_Decryptor(cypher_text,keys,flag)

	return render_template('Decrypt1.html',cypher_text = cypher_text ,keys=keys, plain_text = real_plain_text , passed=passed)





@app.route('/decrypted_stego_image',methods=["POST"])
def decrypted_stego_image():
	c = Crpytography()
	stego = STEANOGRAPHY()
	passed=False
	# file = request.files['file']


	# if file and allowed_file(file.filename):
	
	keys=request.form.get("KEYS")
	filename=request.form.get("FILENAME")
	filename = secure_filename(filename)


		



	print('@@@ filename:  Got is :' + filename)


	

	#Extraxt Cypher txt from stego Image
	option=2
	c_text=""
	directory='static/uploads/'
	cypher_text = stego.Steganography(option,filename,c_text,directory)

	flags=1
	cypher_text,real_plain_text  = c.Crpyto_Decryptor(cypher_text,keys,flags)

	return render_template('Stego.html',cypher_text = cypher_text , keys=keys, plain_text = real_plain_text ,filename=filename)





@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)





@app.route('/team_info')
def team_info():
	return render_template('Team_Info.html')

if __name__ =="__main__":
	app.run(debug=True)










###################################

# 'stego_'+