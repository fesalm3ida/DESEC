#!/usr/share/python
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("200.160.2.80",43))
s.send(("businesscorp.com.br"+"\r\n").encode())
resposta = s.recv(4096).decode('latin-1')
print (resposta)
s.close()
