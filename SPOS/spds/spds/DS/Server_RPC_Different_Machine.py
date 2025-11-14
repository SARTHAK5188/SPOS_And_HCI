from xmlrpc.server import SimpleXMLRPCServer

# Functions to expose
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        # Note: XML-RPC handles errors better if you raise an exception, 
        # but returning a string is valid for basic examples.
        return "Error: Division by zero"

# Setup server
# Binds to 0.0.0.0 to listen on all network interfaces (required for LAN access)
server = SimpleXMLRPCServer(("0.0.0.0", 9000))
print("RPC Server listening on port 9000 on all interfaces...")

server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

# --- FIX: Enable standard XML-RPC system methods ---
server.register_introspection_functions()

server.serve_forever()