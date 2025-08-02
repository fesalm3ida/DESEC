#!/usr/share/python
import socket
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.registro.br",43))
s.send((sys.argv[1]+"\r\n").encode())
resposta = s.recv(4096).decode('latin-1')
print (resposta)
s.close()
