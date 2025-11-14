import socket
import json
import threading

# Function to check password strength
def check_password(password):
    if not isinstance(password, str):
        return "Invalid input"

    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if length < 6:
        return "Very Weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    else:
        return "Very Strong"

# Function to handle client connection
def handle_client(conn, addr):
    print(f"[+] Connected: {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            try:
                request = json.loads(data.decode())
                method = request.get("method")
                params = request.get("params", [])

                if method == "check_password":
                    result = check_password(*params)
                else:
                    result = "Unknown method"

                response = {"result": result}

            except Exception as e:
                response = {"error": str(e)}

            conn.sendall(json.dumps(response).encode())

    print(f"[-] Disconnected: {addr}")

def main():
    host = "0.0.0.0"
    port = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"RPC Password Server running on {host}:{port}")

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
