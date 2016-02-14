#!/usr/bin/python
# -*- coding: utf-8 -*-

# Jesús Galán Barba
# Ing. en Sistemas de Telecomunicaciones

import socket

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.bind(('localhost', 2024))

Socket.listen(1)

while True:
	print 'Waiting for connections'
	(recvSocket, address) = Socket.accept()
	print 'HTTP request received:'
	print recvSocket.recv(1024)
	mensaje = "HTTP/1.1 200 OK\r\n\r\n" + "<html><body><h1>Hola! Eres de esta IP " + str(address[0]) +  " y de este puerto " + str(address[1]) +  "</h1></body></html>" + "\r\n"
	recvSocket.send(mensaje)
	recvSocket.close()
