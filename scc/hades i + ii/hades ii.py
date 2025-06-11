
import sys
import socket
import time

import aes
import binascii

hostname = 'hades-ii.quals.scc2025.ctf.rs'
port = 9110
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname,port))

blah = sock.recv(1024)

key = 0x3030303030303030303030303030303030303030303030303030303030303030


mk_arr = aes.utils.int2arr8bit(key, 32)

cipher = aes.aes(key, 256, mode='ECB')

i = 0
j = 0
for _ in range(0,50):
	print("ROUND : ", i)
	#user_input = input('Write...')
	#input_bytes = user_input.encode('utf-8')
	
	sock.sendall((str(3) + "\n").encode('utf-8'))
	sock.sendall(("3030303030303030303030303030303030303030303030303030303030303030" + "\n").encode('utf-8'))
	time.sleep(1)
	data = sock.recv(1024)
	dec = data.decode()
	text = dec.split()
	
	#for index,value in enumerate(text):
		#print(index, " : ", value)
	
	#Gledamo levi samo
	whole = text[10 + j]
	first_half = whole[:32]
	second_half = whole[32:]

	print(first_half)
	print(second_half)

	dec_first = int(first_half, 16)
	dec_second = int(second_half, 16)

	#print(dec_first)
	#print(dec_second)

	first_arr = aes.utils.int2arr8bit(dec_first, 16)
	second_arr = aes.utils.int2arr8bit(dec_second, 16)

	rez1 = cipher.dec_once(first_arr)
	rez2 = cipher.enc_once(second_arr)

	#print(rez1)
	#print(rez2)
	
	if(rez1 == rez2):
		# Ovo znaci da je levi pseud
		print("Levi je pseud")
		sock.sendall((str(2) + "\n").encode('utf-8'))
	else:
		print("Levi nije pseud")
		sock.sendall((str(1) + "\n").encode('utf-8'))
	
	sock.recv(1024)
	i = i + 1
	
	if j != 3:
		j = 3

print(sock.recv(1024))
