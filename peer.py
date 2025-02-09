import requests
import socket
import threading
import json

TRACKER_URL = "http://localhost:5000"
TRACKER_URL_EXTERNAL = "http://192.168.15.9:5000"

peer_id = "peer1"
pieces = [0, 1, 2]  # Example: Peer has first three pieces

# Announce to tracker
requests.post(f"{TRACKER_URL_EXTERNAL}/announce", json={"peer_id": peer_id, "pieces": pieces})

# Function to handle incoming piece requests
def serve_pieces():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 6000))  # Listen on port 6000
    server.listen(5)
    
    while True:
        conn, addr = server.accept()
        piece_request = conn.recv(1024).decode()
        conn.send(f"Sending piece {piece_request}".encode())  # Send fake data
        conn.close()

threading.Thread(target=serve_pieces, daemon=True).start()

# Request available peers
response = requests.get(f"{TRACKER_URL_EXTERNAL}/get_peers").json()
print("Available Peers:", response)
