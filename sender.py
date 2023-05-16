import socket

HOST = 'localhost'  # The IP address of the receiver
PORT = 8080  # The port on which to communicate

filename = 'sendfile.txt'

with open(filename, 'rb') as f:
    file_data = f.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(file_data)

print(f"{filename} has been sent.")
