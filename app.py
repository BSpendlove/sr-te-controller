from flask import Flask
from controllers.xr_ssh import CiscoXRAPI

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Test"

@app.route("/<string:device>/test_ssh", methods=["POST"])
def test_ssh(device):
    _device = CiscoXRAPI(device)
    return _device.connect()

@app.route("/<string:device>/hostname", methods=["GET"])
def device_hostname(device):
    _device = CiscoXRAPI(device)
    conn = _device.connect()

    if conn["error"]:
        return conn
    
    return {"error": False, "data": [{"hostname": _device.get_hostname()}]}

@app.route("/<string:device>/isis_database", methods=["GET"])
def device_isis_database(device):
    _device = CiscoXRAPI(device)
    conn = _device.connect()

    if conn["error"]:
        return conn

    return {"error": False, "data": _device.get_isis_database()}

@app.route("/<string:device>/isis_neighbors", methods=["GET"])
def device_isis_neighbors(device):
    _device = CiscoXRAPI(device)
    conn = _device.connect()

    if conn["error"]:
        return conn

    return {"error": False, "data": _device.get_isis_neighbors()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
