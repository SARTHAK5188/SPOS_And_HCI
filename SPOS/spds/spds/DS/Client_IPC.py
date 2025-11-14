import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345)) # Same host and port as serverprint("Connected to server. Type 'exit' to quit.")
while True:
    msg = input("You: ")
    client.send(msg.encode())
    if msg.lower() == 'exit':
        break
    response = client.recv(1024).decode()
    print(f"Server: {response}")
client.close()