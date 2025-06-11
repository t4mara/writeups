
import sys
import socket
import time

hostname = 'hades.quals.scc2025.ctf.rs'
port = 9109
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname,port))

blah = sock.recv(1024)

sock.sendall((str(2) + "\n").encode('utf-8'))
sock.sendall((str(2) + "\n").encode('utf-8'))

i = 0
j = 0

for _ in range(0,50):
	print("ROUND : ", i)
	sock.sendall((str(3) + "\n").encode('utf-8'))
	sock.sendall(("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + "\n").encode('utf-8'))
	time.sleep(1)
	data = sock.recv(1024)
	dec = data.decode()
	text = dec.split()
	
	for index,value in enumerate(text):
		print(index, " : ", value)
	
	prvi = text[10 + j]
	drugi = text[15 + j]
	print(prvi, drugi)

	sock.sendall((str(3) + "\n").encode('utf-8'))
	sock.sendall(("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + "\n").encode('utf-8'))
	time.sleep(1)
	data2 = sock.recv(1024)
	dec2 = data2.decode()
	text2 = dec2.split()
	
	for index,value in enumerate(text2):
		print(index, " : ", value)

	treci = text2[10]
	cetvrti = text2[15]
	print(treci, cetvrti)

	if(prvi == treci):
		sock.sendall((str(2) + "\n").encode('utf-8'))
	else:
		sock.sendall((str(1) + "\n").encode('utf-8'))
	sock.recv(1024)
	i = i + 1
	j = 3

print(sock.recv(1024))
