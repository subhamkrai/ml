#!/usr/bin/python3

import  socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

a="subham manish jaydev anand"
b=a.encode('utf-8')

s.sendto(b,("192.168.10.101",9898))

