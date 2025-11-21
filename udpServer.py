import socket

localIP = "127.0.0.1"
localPort = 9997
buffer = 1024

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((localIP, localPort)) # Menyalakan server UDP

print("UDP server up and listening on")

# Listening
while (True):
    data = serverSocket.recvfrom(buffer)
    pesan = data[0]
    ip_address = data[1]

    print("Pesan dari Client: \"{}\"".format(pesan))
    print("IP address Client: \"{}\"".format(ip_address))

    serverSocket.sendto(b"Selamat datang di UDP Server", ip_address)
