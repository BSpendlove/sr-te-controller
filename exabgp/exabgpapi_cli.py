from flask import Flask, request
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

@app.route("/exabgp/cli/version", methods=["GET"])
def version():
    cmd = "exabgpcli version"

    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    return result.stdout

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
