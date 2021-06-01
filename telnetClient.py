import socket
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port=8888

s.connect(('192.168.56.108', port))

data=s.recv(1024)

s.send(b'Hi, I am client. Thankyou connect with me');

print(data)


print("This program allowed you to check the open port of the remote server")
print("*" * 60)

remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("_" * 50)
print("Please wait, scanning remote host", remoteServerIP)
print("_" * 50)

try:
    for port in range(1,1025):
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      result = sock.connect_ex(('192.168.56.108', port))
      if result == 0:
         print("Port {}:          Open".format(port))
         print("Therefore, it shows only port {} is open.".format(port))
         sock.close()

except KeyboardInterrupt:
       print("You pressed Ctrl+C")
       sys.exit()

except socket.gaierror:
       print('Hostname could not be resolved. Exiting')
       sys.exit()

except socket.error:
       print("Couldn't connect to server")
       sys.exit()


s.close()
