from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/api/v1/exabgp", methods=["POST"])
def exabgp():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}

    data = request.get_json()
    print(json.dumps(data, indent=4))

    if data["type"] == "state":
        #Handle BGP State message
        pass
    if data["type"] == "update":
        #Handle BGP Update message
        pass

    return "Test"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)