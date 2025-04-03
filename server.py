import socket
import os
import platform
from _thread import *
def shutdown_server():
    # Create TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5050))  # Listen on all interfaces
    server.listen(1)
    print("[SERVER LISTENING] on port 5050...")
    def threadedClient(conn):
        while True:
            clientMessage = conn.recv(64).decode('utf-8)
        
    while True:
        conn, addr = server.accept()
        print(f"Connection from {addr}")
        
        # Receive shutdown command
       
        client_socket.close()
    server.close()

shutdown_server()
