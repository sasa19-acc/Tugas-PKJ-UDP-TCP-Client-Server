import socket

target_host = "127.0.0.1"
target_port = 9997 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"Hello UDP Server", (target_host, target_port)) # Mengirim data

# Menerima data
data, address = client.recvfrom(4096)
print("Respon dari server: \"{}\"".format(data.decode()))

client.close()