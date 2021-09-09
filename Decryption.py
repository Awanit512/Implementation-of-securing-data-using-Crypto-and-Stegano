from Preprocessing  import Preprocessing
import Encryption






class Decryption(Preprocessing):


	def Decrypt(self,C_Is,KEYS):
		#FIRST HALF  #tuples of Key and C_Is cypher text each of 32 bits are passed
		CI1 ,CI2, CI3, CI4 = C_Is
		K1,K2,K3,K4 = KEYS

		CI2 = self.xor_32bits(CI2,CI1)
		CI4 = self.xor_32bits(CI4,CI3)
		CI1 = self.anti_clockwise_CircularShift(CI1,2)
		CI3 = self.anti_clockwise_CircularShift(CI3,2)
		CI1 = self.xor_32bits(CI1,CI2)
		CI3 = self.xor_32bits(CI4,CI3)
		CI2 = self.clockwise_CircularShift(CI2,2)
		CI4 = self.clockwise_CircularShift(CI4,2)	



		#SECOND HALF

		CI3 = self.xor_32bits(K4,CI3)
		CI4 = self.xor_32bits(CI4,K2)
		CI3 = self.anti_clockwise_CircularShift(CI3,2)
		CI4 = self.anti_clockwise_CircularShift(CI4,2)
		CI4 = self.xor_32bits(CI2,CI4)
		CI3 = self.xor_32bits(CI1,CI3)
		EI2 = CI4
		EI4 = CI3

		CI1 = self.xor_32bits(CI1,K3)
		CI2 = self.xor_32bits(CI2,K1)
		CI2 = self.clockwise_CircularShift(CI2,2)
		CI1 = self.clockwise_CircularShift(CI1,2)
		EI1 = CI2
		EI3 = CI1


		return (EI1,EI2,EI3,EI4)

















	# #tuples of Key and C_T cypher text each of 32 bits are passed
	# def first_half_Decrpt(self,C_T,KEYS):
	# 	C1,C4,C2,C3 = C_T
	# 	K1,K2,K3,K4 = KEYS
	# 	C4 = self.xor_32bits(C4,C1)
	# 	C1 = self.anti_clockwise_CircularShift(C1,2)
	# 	C4 = self.xor_32bits(C4,K4)

	# 	O1 = self.xor_32bits(C1,C4)
	# 	O2 = self.clockwise_CircularShift(C4,3)

	# 	C3 = self.xor_32bits(C2,C3)
	# 	C2 = self.xor_32bits(C2,C3)

	# 	O3 = self.clockwise_CircularShift(C2,3) 
		

	# 	O4 = self.xor_32bits(C3,K3)
		
	# 	return(O1,O3,O4,O2)




	# #tuples of Key and C_T' of first half decryption's cypher text each of 32 bits are passed with keys
	# def second_half_Decrpt(self,C_T_,KEYS):
	# 	O1,O2,O3,O4 = C_T_
	# 	K1,K2,K3,K4 = KEYS

	# 	O1 = self.xor_32bits(O1,K1)
	# 	O2 = self.clockwise_CircularShift(O2,4)
	# 	O3 = self.anti_clockwise_CircularShift(O3,4)

	# 	O3 = self.xor_32bits(O3,K2)
	# 	E4 = self.xor_32bits(O4,O3)
	# 	E3 = self.clockwise_CircularShift(O3,2)


	# 	E2 = self.xor_32bits(O2,O1)
	# 	E1 = self.anti_clockwise_CircularShift(O1,2)
		
		
	# 	return(E1,E2,E3,E4)  #plain text corresponding to cypher text of 128 bits each cypher text is of 32 bits broken into plain text of each 32 bits.



















def main():
	pass













if __name__ == "__main__" :
	print("Start...\n")
	main()
