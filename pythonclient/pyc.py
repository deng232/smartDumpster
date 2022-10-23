import socket;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket successfully created")
port = 3000
s.connect(('127.0.0.1',3000))
print ("socket connected to %s" %(port))
s.send(b'hello')
while True :
    sc = s.recv(1024).decode()
    print (sc)
    for i in range(10):
        s.send(bytes(str(i).encode()))
        