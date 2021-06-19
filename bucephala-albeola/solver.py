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
HOST, PORT = "bucephala-albeola.hsc.tf", 1337
s, f = sock(HOST, PORT)
read_until(f)
read_until(f)

candi = "abcdefghiklmnopqrstuvwxyz"
cnt = []
for i in range(29):
	tmp = [0 for i in range(111)]
	cnt.append(tmp)
for c in candi:
	read_until(f,"key: ")
	s.send(c.encode()+b"\n")
	print("key:",c)
	recv_m = read_until(f).split()
	print(" ".join(recv_m))
	for i in range(29):
		cnt[i][int(recv_m[i+1])] = c
last = [0 for i in range(111)]
ans = []
form = ""
for k in range(29):
	ch = True
	for i in range(11):
		for j in range(1,11):
			if cnt[k][i*10+j] == 0: continue
			else:
				if ch:
					#print(i*10+j,chr(int(str(i*10+j),16)))
					last[i*10+j] += 1
					ans.append(i*10+j)
				form += cnt[k][i*10+j]
				ch = False
				print(cnt[k][i*10+j],end="")
		if not ch: print()
	print()

s1,t1 = 0,0
for i in range(11):
	for j in range(1,11):
		if last[i*10+j] == 0: continue
		else:
			print(i,j)
			s1 = i
			t1 = j
			break
	if s1 > 0 and t1 > 0: break
#form = "abcdeghiklmnopqrstuvwxyz"
for x in ans:
	s0 = x//10
	t0 = x%10
	y = (s0-s1)*5+(t0-t1)
	print(form[y],end="")
print()


#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() or .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

