from flask import Flask, request

app = Flask(__name__)

@app.route("/api/v1/test", methods=["POST"])
def index():
    if not request.is_json:
        return {"error": True, "message": "Incorrect format (must be JSON)."}
    data = request.get_json()
    print(data)
    return {"error": False}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)