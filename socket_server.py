#!/usr/bin/env python
#coding:utf-8



import socket
import os
import time


HOST = ''
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()                     #connection with the client server

f = open('IP_address.txt')
while True:	
	IP_address = f.readline()
	if len(IP_address) == 0:
		break
# print IP_address                          #configure the IP address

# print 'wanningxi'

while True: 
	
	data = conn.recv(4096)
	if addr in IP_address:
		print 'Connected by', addr 				
		if not data:
				break
		print data,time.time()
	else:
		print 'I didn\'t monitor this server'
conn.close()                                #print information of monitor