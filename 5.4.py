import socket

s = socket.socket()

host_name = socket.gethostname() 
IPADDRESS = socket.gethostbyname(host_name) 

PORT = 9999
print("IP address of the server: ", IPADDRESS)
print("Server is listening on port: ", PORT)
print("\nWaiting for connection from a client...")

s.bind(('', PORT))

s.listen(10)

while True:
    
    conn, addr = s.accept()

    msg = "\n\nHi, Client [IP address: "+ addr[0] + "], \nThank you for using our storage service. \nYour files are safe with us.\n-Server\n"    
    conn.send(msg.encode())
    
    filename = conn.recv(1024).decode("utf-8")
    file = open(filename, "wb")
   
    RecvData = conn.recv(99999)
    
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(99999)

    file.close()
    print("\nFile has been copied successfully \n")

    conn.close()
    print("Server closed the connection \n")

    break
