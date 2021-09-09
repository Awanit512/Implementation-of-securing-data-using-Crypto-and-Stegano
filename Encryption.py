import sys
from Preprocessing  import Preprocessing 




class Encryption(Preprocessing):

	def Encrypt(self,EI_S,KEYS):



		#FIRST HALF #tuples of Key and EI_S each of 32 bits broken by method Preprocessing.Convert128_to_32bits( args)
		E1,E2,E3,E4 = EI_S
		K1,K2,K3,K4 = KEYS
		#print(f"E1 : {E1}\n  E2: {E2}  \nE3:{E3} \n  E4:{E4} ")
		#print(f"K1 : {K1}\n  K2: {K2}  \nK3:{K3} \n  K4:{K4} ")
		E1 = self.anti_clockwise_CircularShift(E1,2)
		#print(f"Anti 2  of E1 : {}")
		E1 = self.xor_32bits(E1,K1)
		E3 = self.anti_clockwise_CircularShift(E3,2)
		E3 = self.xor_32bits(K3,E3)

		E2 = self.xor_32bits(E2,E1)
		E4 = self.xor_32bits(E3,E4)
		E2 = self.clockwise_CircularShift(E2,2)
		E4 = self.clockwise_CircularShift(E4,2)
		E2 = self.xor_32bits(K2,E2)
		E4 = self.xor_32bits(K4,E4)



		#SECOND HALF
		E1 = self.anti_clockwise_CircularShift(E1,2)
		E2 = self.anti_clockwise_CircularShift(E2,2)

		E3 = self.xor_32bits(E1,E3)
		E4 = self.xor_32bits(E4,E2)
		E3 = self.clockwise_CircularShift(E3,2)
		E4 = self.clockwise_CircularShift(E4,2)
		CI1 = E3
		CI3 = E4

		E2 = self.xor_32bits(CI3,E2)
		CI4 = E2
		E1 = self.xor_32bits(CI1,E1)
		CI2 = E1

		return (CI1,CI2,CI3,CI4)












	# #tuples of Key and EI each of 32 bits broken by method Preprocessing.Convert128_to_32bits( args)
	# def first_half_Encrpt(self,EI_S,KEYS):
	# 	E1,E2,E3,E4 = EI_S
	# 	K1,K2,K3,K4 = KEYS
	# 	E1 = self.clockwise_CircularShift(E1,2)
	# 	E3 = self.anti_clockwise_CircularShift(E3,2)
	# 	E2 = self.xor_32bits(E2,E1)
	# 	O4 = self.xor_32bits(E4,E3)

	# 	O1 = self.xor_32bits(E1,K1)
	# 	E3 = self.xor_32bits(E3,K2)
	# 	O3 = self.clockwise_CircularShift(E3,4)
	# 	O2 = self.anti_clockwise_CircularShift(E2,4)
		
	# 	return (O1,O2,O3,O4)






	# #tuples of Key and EI each of 32 bits broken by method Preprocessing.Convert128_to_32bits( args)
	# def second_half_Encrpt(self,OI_S,KEYS):
	# 	O1,O3,O4,O2 = OI_S
	# 	K1,K2,K3,K4 = KEYS
	# 	O2 = self.anti_clockwise_CircularShift(O2,3) 
	# 	O1 = self.xor_32bits(O1,O2)
	# 	O2 = self.xor_32bits(O2,K4)

	# 	C1 = self.clockwise_CircularShift(O1,2) 
	# 	C2 = self.xor_32bits(O2,C1)

	# 	O3 = self.anti_clockwise_CircularShift(O3,3)
	# 	O4 = self.xor_32bits(O4,K3)

	# 	C3 = self.xor_32bits(O3,O4)
	# 	O4 = self.anti_clockwise_CircularShift(O4,2)

	# 	C4 = self.xor_32bits(O4,C3)
	# 	return (C1,C2,C3,C4)   #cypher text corresponding to our data of 128 bits each cypher text is of 32 bits

























def main():
	pass














if __name__ == "__main__" :
	print("Start...\n")
	main()
