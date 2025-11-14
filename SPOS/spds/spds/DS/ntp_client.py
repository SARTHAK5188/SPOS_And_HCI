import socket
import time

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


T1 = time.time()
client_socket.sendto(b"Time Request", (SERVER_HOST, SERVER_PORT))


data, _ = client_socket.recvfrom(1024)
T4 = time.time()  


T2, T3 = map(float, data.decode().split(','))


delay = (T4 - T1) - (T3 - T2)
offset = ((T2 - T1) + (T3 - T4)) / 2


adjusted_time = time.time() + offset


print("\n----- NTP Clock Synchronization (Numerical Values) -----")
print(f"T1 (Request Sent):     {T1}")
print(f"T2 (Request Received): {T2}")
print(f"T3 (Reply Sent):       {T3}")
print(f"T4 (Reply Received):   {T4}")
print(f"Round Trip Delay (d):  {delay:.6f} seconds")
print(f"Clock Offset (θ):      {offset:.6f} seconds")
print(f"Original Client Time:  {time.time()}")
print(f"Adjusted Client Time:  {adjusted_time}")
print("--------------------------------------------------------")