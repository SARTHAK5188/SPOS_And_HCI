import xmlrpc.client

# --- MODIFIED SECTION ---
# 1. Get the server IP from user input
server_ip = input("Enter the server's IP address (e.g., 127.0.0.1 or 192.168.1.100): ")
server_port = 9000

# 2. Construct the connection string using the provided IP
server_url = f"http://{server_ip}:{server_port}/"

# Connect to RPC server
try:
    proxy = xmlrpc.client.ServerProxy(server_url)
    # Ping the server with a test call to confirm connection
    # Note: System methods like 'listMethods' are standard for XML-RPC
    proxy.system.listMethods() 
    print(f"Connected to RPC Server at {server_ip}:{server_port}.")
except ConnectionRefusedError:
    print(f"Error: Connection refused. Ensure the server is running at {server_ip}:{server_port}.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()
# --- END MODIFIED SECTION ---

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 5:
        print("Exiting...")
        break
        
    # Get numbers (Input validation added for robustness)
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered. Please try again.")
        continue

    if choice == 1:
        print("Result:", proxy.add(a, b))
    elif choice == 2:
        print("Result:", proxy.subtract(a, b))
    elif choice == 3:
        print("Result:", proxy.multiply(a, b))
    elif choice == 4:
        print("Result:", proxy.divide(a, b))
    else:
        print("Invalid choice")