import socket
import json

def call_password_checker(password):
    host = "127.0.0.1"
    port = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Create the RPC request
    request = {"method": "check_password", "params": [password]}
    s.sendall(json.dumps(request).encode())

    # Receive the response
    data = s.recv(1024)
    response = json.loads(data.decode())
    s.close()

    if "result" in response:
        print(f"Password Strength: {response['result']}")
    else:
        print("Error:", response.get("error"))

if __name__ == "__main__":
    while True:
        password = input("Enter password (or type 'exit' to quit): ")

        if password.lower() == "exit":
            break

        call_password_checker(password)
