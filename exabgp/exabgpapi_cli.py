from flask import Flask, request
from shlex import quote
import subprocess

"""
This Flask App is just a test
"""

app = Flask(__name__)

@app.route("/exabgp/cli/show_neighbor_summary", methods=["GET"])
def show_neighbors_summary():
    cmd = "exabgpcli show neighbor summary"

    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    return result.stdout

@app.route("/exabgp/cli/announce/label", methods=["POST"])
def announce_label():
    if not request.is_json:
        return {"error": True, "message": "Invalid message type, JSON should be used..."}

    cmd = None
    data = request.get_json()

    if not "command" in data:
        return {"error": True, "message": "command not found."}

    cmd = "exabgpcli {}".format(quote(data["command"]))

    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    if not result:
        return None

    return {"error": False, "stdout": str(result.stdout)}

@app.route("/exabgp/cli/version", methods=["GET"])
def version():
    cmd = "exabgpcli version"

    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    return result.stdout

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
