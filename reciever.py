import socket

HOST = 'localhost'  # The IP address of the receiver
PORT = 8080  # The port on which to communicate

filename = 'example.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")
        file_data = conn.recv(1024)
        with open(filename, 'wb') as f:
            f.write(file_data)

print(f"{filename} has been received.")
