from Crypto.Util.number import *
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib

# --- common funcs ---
def sock(remoteip, remoteport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((remoteip, remoteport))
	return s, s.makefile('rw')

def read_until(f, delim='\n'):
	data = ''
	while not data.endswith(delim):
		data += f.read(1)
	return data

	
#HOSTはIPアドレスでも可
HOST, PORT = "canis-lupus-familiaris-bernardus.hsc.tf", 1337
s, f = sock(HOST, PORT)
for _ in range(40-7+2): read_until(f)
#print(read_until(f))
for cnt in range(100):
	recv_m = read_until(f,"peptide? ").split()
	enc = recv_m[1]
	if "J" in recv_m[1] or "O" in recv_m[1] or "U" in recv_m[1] or "X" in recv_m[1]:
		print("F")
		s.send(b"F\n")
		print(read_until(f))
		iv = read_until(f).split()[-1]
		print("iv:",iv)
		riv = ""
		for i in range(len(enc)):
			if enc[i] == "J":
				riv += iv[:2*i]
				t = ord("J")^ord("A")^int(iv[2*i:2*i+2],16)
				t = hex(t)[2:]
				if len(t) == 1: t = "0"+t
				riv += t + iv[2*i+2:]
				break
			if enc[i] == "O":
				riv += iv[:2*i]
				t = ord("O")^ord("A")^int(iv[2*i:2*i+2],16)
				t = hex(t)[2:]
				if len(t) == 1: t = "0"+t
				riv += t + iv[2*i+2:]
				break
			if enc[i] == "U":
				riv += iv[:2*i]
				t = ord("U")^ord("A")^int(iv[2*i:2*i+2],16)
				t = hex(t)[2:]
				if len(t) == 1: t = "0"+t
				riv += t + iv[2*i+2:]
				break
			if enc[i] == "X":
				riv += iv[:2*i]
				t = ord("U")^ord("A")^int(iv[2*i:2*i+2],16)
				t = hex(t)[2:]
				if len(t) == 1: t = "0"+t
				riv += t + iv[2*i+2:]
				break
		read_until(f,"use: ")
		print("modified iv:",riv)
		s.send(riv.encode()+b"\n")
		print(read_until(f))	
		
	else:
		print("T")
		s.send(b"T\n")
		print(read_until(f))

while True: print(read_until(f))

#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() or .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

