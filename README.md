# Design and Implementation of securing data using Cryptography and Steganography
<p>It is a A Python based application with use of flask a microservice based
framework to demonstrate the combination of cryptography that is based on symmetric key and
steganography that is based on modified LSB which helps to provide security to confidential data over
an unsecured network.</p>

# Project Team Members :
<ul>
<li><b>Awanit Ranjan (181CO161) </b></li>
<li><b>Rutwik Mulay (181CO144)</b></li>
<li><b>Kshitij Raj (181CO129) </b></li>
</ul>

<br>


Feel Free to head to this Youtube Video  for demo of the project : https://youtu.be/N4Kap2nE2Pc 

# METHODOLOGY : 
<div>
<p>
  First, we take the original data and encrypt it into
ciphertext by utilizing the proposed symmetric cryptography method in which we will break the 128 bits
into 4 equal groups of 32 bit each this 32-bit block will be undergone some circular shift and xor
operations with secret keys . ( These ideas are inspired by [1] and [2] ). After this, the encrypted data will
be embedded in a Cover Image by use of proposed steganography strategy which is utilizing least
significant bit (LSB) [ In this we are think of going with a mixture of LSB-1, LSB-2, LSB-3 (i.e storing at
first, second, and a third bit from the least significant side) alternatingly. ] to finally create a new image
which is a stego content this is sent over the channel and at receiver side the same process will occur
but in reverse, starting from extracting encrypted content from stego and finally decrypting using
proposed decryption algorithm again inspired by [1] and [2]. Although ideas are inspired, we will use our
own proposed architecture for encryption and decryption finally converting into an application for
sending data over insecure channels.
</p>
</div>



# REFERENCES

[1] Marwa E. Saleh Abdel Magied A. Aly Fatma A. Omara. CSE from Minia University, ​ Data Security Using Cryptography and
Steganography Techniques . ​ International Journal of Advanced Computer Science and applications, 2016.

[2] Ms. Hemlata Sharma, Ms. MithleshArya, and Mr. Dinesh Goyal. Department of CSE ​ Secure Image Hiding Algorithm using
Cryptography and Steganography. 2013
