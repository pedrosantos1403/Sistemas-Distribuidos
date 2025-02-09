from flask import Flask, request, jsonify

app = Flask(__name__)

# Stores peer information (which peer has which pieces)
peers = {}

@app.route("/announce", methods=["POST"])
def announce():
    data = request.json
    peer_id = data["peer_id"]
    pieces = data["pieces"]

    # Store the peer's available pieces
    peers[peer_id] = pieces

    # Log the connection
    print(f"[TRACKER] Peer {peer_id} registered with pieces: {pieces}")

    return jsonify({"status": "registered", "peers": peers})

@app.route("/get_peers", methods=["GET"])
def get_peers():
    print("[TRACKER] A peer requested the list of available peers.")
    return jsonify(peers)

if __name__ == "__main__":
    print("[TRACKER] Server started on port 5000, listening for external connections")
    app.run(host="0.0.0.0", port=5000)

