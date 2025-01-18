import socket
import threading
from queue import Queue

# Take IP as input from user
target = input("Enter the host IP to scan: ")

# Create a queue
q = Queue()

# scan a port
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout after 1 second
        result = sock.connect_ex((target, port))  # Try to connect to the port
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()
    except socket.error:
        pass

# Worker function to handle multiple threads
def worker():
    while True:
        port = q.get()
        scan_port(port)
        q.task_done()

# this block will create threads (choose 100 threads for better performance)
for _ in range(100):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# this block will Enqueue all ports (1 to 65535)
for port in range(1, 65536):
    q.put(port)

# Wait for the queue to empty
q.join()

print("Scanning complete!")