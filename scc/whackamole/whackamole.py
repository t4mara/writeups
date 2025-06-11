import sys
import socket
import time

hostname = 'whack-a-mole.warmup.scc2024.ctf.rs'
port = 9001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname,port))

data = sock.recv(1024)
print(data)
data = data.decode()
text = data.split()

print("Prva: ")
prva = int(text[55])

print(prva)
print("Druga :")
druga = int(text[56])

print(druga)
print("Treca: ")
treca = int(text[57])

print(treca)
print("M je: ")
m = int(text[15])

print(m)


gore = (treca - druga) % m
dole = (druga - prva) % m
dole_inv = pow(dole, -1, m)
a = (gore * dole_inv) % m
print("A je: ", a)

c = (druga - prva * a) % m
print("C je: ", c)

prethodni = treca

for i in range(0,5):
	noviseed = ((prethodni*a)+c) % m
	sock.sendall((str(int(noviseed)) + "\n").encode('utf-8'))
	time.sleep(1)
	print(sock.recv(1024))
	print("Rezultat: ", int(noviseed))
	prethodni = noviseed

print(sock.recv(1024))

org = (prva - c) * pow(a, -1, m) % m
print(org)
