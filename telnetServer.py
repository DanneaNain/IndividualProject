import socket

#Create a socket object
s=socket.socket()
print("Socket is succesfully connected")

#Insert any port number
port=8888

#Bind
s.bind(('' ,port))
print("Socket is binded to "+str(port))

#Listen
s.listen(5)
print("Socket is listening")

while True:

   c, addr=s.accept()

   print("Got connection from"+str(addr))

   c.send(b"Hi, this is my server :)")

   c.send(b'Thanks to you too !')
   buffer=c.recv(1024)
   print(buffer)


c.close()
