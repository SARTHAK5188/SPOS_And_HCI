import socket
import time

HOST = '127.0.0.1'  
PORT = 12345       


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("NTP Server is running... Waiting for client requests...\n")

while True:
    data, addr = server_socket.recvfrom(1024)
    if data:

        T2 = time.time()   
        time.sleep(0.05)   
        T3 = time.time()  


        msg = f"{T2},{T3}"
        server_socket.sendto(msg.encode(), addr)

        print(f"Sent timestamps to client {addr}: T2={T2}, T3={T3}")