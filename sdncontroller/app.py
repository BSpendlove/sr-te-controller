from flask import Flask, request
from views import exabgptype as exabgp_view

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "test"

if __name__ == "__main__":
    app.register_blueprint(exabgp_view.bp)
    app.run(host="0.0.0.0", port=5000, debug=True)
