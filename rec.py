#!/usr/bin/python3

import  socket,time,json
from collections import Counter

rec_ip="127.0.0.1"
myport=9999
#                 ipv4       ,  for UDP   
#   only  for rec                      
#  below method with argument creating a socket called  s 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  now connecting ip  and port 
s.bind((rec_ip,myport)) 
#  buffer size 
c = []

timeout = time.time() + 10
while time.time() < timeout:
	a = s.recvfrom(1000)[0]
	d = a.decode('utf-8')
	b = d.split()
	for i in range(len(b)):
		c.append(b[i])	
#		print(c)	

d=list(set(c))
#print(d)
result= Counter()
for i in d:
	result[i]=c.count(i)
q=dict(result)
print(q)
print(list(q.values()))
print(list(q.keys()))
t=list(q.values())
y=list(q.keys())
'''with open('xaxis.txt','w') as f:     
	for i in t:
		f.write('%s\n'%i)
with open('yaxis.txt','w') as f:    
	for i in d:
		f.write('%s\n'%i)
with open('xaxis.txt','w') as f:
	json.dump(t,f)
with open('yaxis.txti','w') as f:
	json.dump(y,f)'''
import matplotlib.pyplot as plt
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.bar(y,t, width=0.7,color=['r','g'])
plt.show()



